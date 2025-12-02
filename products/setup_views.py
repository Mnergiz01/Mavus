from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.management import call_command
from .models import Category, Product, ProductImage
import os


@csrf_exempt
@require_http_methods(["POST"])
def setup_production_database(request):
    """
    One-time setup endpoint for production database.
    Requires SECRET_SETUP_KEY in environment or request.

    Usage:
    POST /api/setup-production/
    Body: {"secret_key": "your-secret-key"}
    """

    # Get secret key from environment
    secret_key = os.getenv('SECRET_SETUP_KEY', 'mavus-setup-2024')

    # Check authorization
    provided_key = request.POST.get('secret_key') or request.headers.get('X-Setup-Key')

    if provided_key != secret_key:
        return JsonResponse({
            'success': False,
            'error': 'Unauthorized: Invalid secret key'
        }, status=401)

    try:
        # Get current counts
        old_categories = Category.objects.count()
        old_products = Product.objects.count()

        # Clear existing data
        Product.objects.all().delete()
        Category.objects.all().delete()
        ProductImage.objects.all().delete()

        # Run migrations (safe to run multiple times)
        call_command('migrate', verbosity=0)

        # Load sample data
        call_command('create_sample_data')

        # Get new counts
        new_categories = Category.objects.count()
        new_products = Product.objects.count()

        return JsonResponse({
            'success': True,
            'message': 'Production database successfully updated!',
            'old_data': {
                'categories': old_categories,
                'products': old_products
            },
            'new_data': {
                'categories': new_categories,
                'products': new_products
            }
        })

    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)


@require_http_methods(["GET"])
def setup_status(request):
    """Check current database status"""

    categories_count = Category.objects.count()
    products_count = Product.objects.count()
    parent_categories = Category.objects.filter(parent=None)

    parent_cats_info = []
    for cat in parent_categories:
        parent_cats_info.append({
            'name': cat.name,
            'children_count': cat.children.count()
        })

    return JsonResponse({
        'database_status': {
            'total_categories': categories_count,
            'total_products': products_count,
            'parent_categories': len(parent_cats_info),
            'parent_categories_detail': parent_cats_info
        }
    })
