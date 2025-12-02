from rest_framework import viewsets, filters
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Product
from .serializers import CategorySerializer, ProductListSerializer, ProductDetailSerializer
import requests
from decimal import Decimal
from bs4 import BeautifulSoup
import re
import socketio
import time
from threading import Event


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    lookup_field = 'slug'

    def get_queryset(self):
        # Sadece ana kategorileri (parent=None) döndür
        return Category.objects.filter(parent=None)


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.filter(is_available=True)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category__slug', 'metal_type', 'karat', 'is_featured', 'is_best_seller', 'is_recommended']
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'created_at', 'name']
    ordering = ['-created_at']
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductDetailSerializer
        return ProductListSerializer

    @action(detail=False, methods=['get'])
    def featured(self, request):
        featured_products = self.queryset.filter(is_featured=True)[:6]
        serializer = self.get_serializer(featured_products, many=True)
        return Response(serializer.data)


def fetch_haremaltin_rates():
    """
    Fetch exchange rates from haremaltin.com using Socket.IO
    """
    rates_data = {}
    connected = Event()
    data_received = Event()

    sio = socketio.Client(logger=False, engineio_logger=False)

    @sio.on('connect')
    def on_connect():
        connected.set()

    @sio.on('price_changed')
    def on_price_changed(data):
        try:
            # Parse the received data
            if isinstance(data, dict) and 'data' in data:
                price_data = data['data']

                # USD/TRY
                if 'USDTRY' in price_data:
                    usd_data = price_data['USDTRY']
                    rates_data['USD'] = {
                        'buying': float(usd_data.get('alis', 0)),
                        'selling': float(usd_data.get('satis', 0)),
                        'code': 'USD',
                        'name': 'Amerikan Doları'
                    }

                # EUR/TRY
                if 'EURTRY' in price_data:
                    eur_data = price_data['EURTRY']
                    rates_data['EUR'] = {
                        'buying': float(eur_data.get('alis', 0)),
                        'selling': float(eur_data.get('satis', 0)),
                        'code': 'EUR',
                        'name': 'Euro'
                    }

                # Gold (Gram)
                if 'ALTIN' in price_data:
                    gold_data = price_data['ALTIN']
                    rates_data['GOLD'] = {
                        'buying': float(gold_data.get('alis', 0)),
                        'selling': float(gold_data.get('satis', 0)),
                        'code': 'GOLD',
                        'name': 'Altın (Gram)',
                        'unit': 'TL/Gram'
                    }

                # Check if we have enough data
                if len(rates_data) >= 3:
                    data_received.set()
        except Exception as e:
            print(f"Error parsing haremaltin data: {e}")

    try:
        # Connect to haremaltin Socket.IO server
        sio.connect('https://socketweb.haremaltin.com:443', transports=['websocket'])

        # Wait for connection (max 3 seconds)
        connected.wait(timeout=3)

        # Wait for data (max 5 seconds)
        data_received.wait(timeout=5)

        sio.disconnect()

        return rates_data if rates_data else None

    except Exception as e:
        print(f"Haremaltin Socket.IO error: {e}")
        try:
            sio.disconnect()
        except:
            pass
        return None


@api_view(['GET'])
def exchange_rates(request):
    """
    Fetch live exchange rates from haremaltin.com and TCMB
    """
    try:
        rates = {}

        # Try to fetch from haremaltin.com first
        harem_rates = fetch_haremaltin_rates()
        if harem_rates:
            rates.update(harem_rates)
            source = 'Harem Altın'
        else:
            source = 'TCMB'

        # Fetch USD and EUR from TCMB as fallback or primary source
        if 'USD' not in rates or 'EUR' not in rates:
            try:
                tcmb_url = "https://www.tcmb.gov.tr/kurlar/today.xml"
                response = requests.get(tcmb_url, timeout=5)
                if response.status_code == 200:
                    import xml.etree.ElementTree as ET
                    root = ET.fromstring(response.content)

                    for currency in root.findall('Currency'):
                        code = currency.get('CurrencyCode')
                        if code in ['USD', 'EUR']:
                            forex_buying = currency.find('ForexBuying')
                            forex_selling = currency.find('ForexSelling')

                            if forex_buying is not None and forex_selling is not None:
                                rates[code] = {
                                    'buying': float(forex_buying.text),
                                    'selling': float(forex_selling.text),
                                    'code': code,
                                    'name': 'Amerikan Doları' if code == 'USD' else 'Euro'
                                }
            except Exception as e:
                print(f"TCMB fetch error: {e}")

        # If still no data, use fallback rates
        if not rates:
            rates = {
                'USD': {'buying': 34.20, 'selling': 34.30, 'code': 'USD', 'name': 'Amerikan Doları'},
                'EUR': {'buying': 37.10, 'selling': 37.20, 'code': 'EUR', 'name': 'Euro'},
                'GOLD': {'buying': 2850.00, 'selling': 2900.00, 'code': 'GOLD', 'name': 'Altın (Gram)', 'unit': 'TL/Gram'}
            }
            source = 'Fallback'

        return Response({
            'success': True,
            'rates': rates,
            'source': source
        })

    except Exception as e:
        return Response({
            'success': False,
            'error': str(e),
            'rates': {
                'USD': {'buying': 34.20, 'selling': 34.30, 'code': 'USD', 'name': 'Amerikan Doları'},
                'EUR': {'buying': 37.10, 'selling': 37.20, 'code': 'EUR', 'name': 'Euro'},
                'GOLD': {'buying': 2850.00, 'selling': 2900.00, 'code': 'GOLD', 'name': 'Altın (Gram)', 'unit': 'TL/Gram'}
            },
            'source': 'fallback'
        }, status=200)
