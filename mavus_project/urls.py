"""
URL configuration for mavus_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from products.api_views import CategoryViewSet, ProductViewSet, exchange_rates

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path("admin/", admin.site.urls),  # Gizli admin URL
    path("api/", include(router.urls)),
    path("api/exchange-rates/", exchange_rates, name="exchange_rates"),
    path("api/products/", ProductViewSet.as_view({'get': 'list'}), name="product-list"),
    path("api/products/<int:pk>/", ProductViewSet.as_view({'get': 'retrieve'}), name="product-detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
