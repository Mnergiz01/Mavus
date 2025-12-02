#!/usr/bin/env python
"""
Render PostgreSQL database'e local'den bağlanıp setup yapmak için script
"""
import os
import sys
import django

# Render DATABASE_URL'inizi buraya yapıştırın
RENDER_DATABASE_URL = input("Render DATABASE_URL'inizi girin (Internal Database URL): ")

# Django settings'i ayarla
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mavus_project.settings')
os.environ['DATABASE_URL'] = RENDER_DATABASE_URL

# Django'yu setup et
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from django.contrib.auth import get_user_model
from products.models import Category, Product, ProductImage

User = get_user_model()

def create_superuser():
    """Admin kullanıcısı oluştur"""
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@mavus.com',
            password='admin123'
        )
        print("✅ Admin kullanıcısı oluşturuldu (username: admin, password: admin123)")
    else:
        print("ℹ️  Admin kullanıcısı zaten mevcut")

def create_sample_data():
    """Örnek kategoriler ve ürünler oluştur"""
    # Ana Kategoriler
    categories_data = [
        {'name': 'Altın Kolye', 'slug': 'altin-kolye'},
        {'name': 'Altın Yüzük', 'slug': 'altin-yuzuk'},
        {'name': 'Altın Bileklik', 'slug': 'altin-bileklik'},
        {'name': 'Altın Küpe', 'slug': 'altin-kupe'},
    ]

    categories = {}
    for cat_data in categories_data:
        cat, created = Category.objects.get_or_create(
            slug=cat_data['slug'],
            defaults={'name': cat_data['name']}
        )
        categories[cat_data['slug']] = cat
        if created:
            print(f"✅ Kategori oluşturuldu: {cat.name}")

    # Örnek Ürünler
    products_data = [
        {
            'name': 'Altın Kolye Model 1',
            'slug': 'altin-kolye-1',
            'category': 'altin-kolye',
            'price': 15000,
            'metal_type': 'gold',
            'karat': '22',
            'weight': 10.5,
            'description': 'Özel tasarım 22 ayar altın kolye',
            'is_featured': True,
        },
        {
            'name': 'Altın Yüzük Model 1',
            'slug': 'altin-yuzuk-1',
            'category': 'altin-yuzuk',
            'price': 8000,
            'metal_type': 'gold',
            'karat': '18',
            'weight': 5.2,
            'description': '18 ayar altın yüzük',
            'is_best_seller': True,
        },
        {
            'name': 'Altın Bileklik Model 1',
            'slug': 'altin-bileklik-1',
            'category': 'altin-bileklik',
            'price': 25000,
            'metal_type': 'gold',
            'karat': '22',
            'weight': 18.0,
            'description': '22 ayar altın bileklik',
            'is_recommended': True,
        },
    ]

    for prod_data in products_data:
        cat_slug = prod_data.pop('category')
        prod, created = Product.objects.get_or_create(
            slug=prod_data['slug'],
            defaults={
                **prod_data,
                'category': categories[cat_slug]
            }
        )
        if created:
            print(f"✅ Ürün oluşturuldu: {prod.name}")

if __name__ == '__main__':
    print("🚀 Render veritabanı setup başlıyor...")
    print()

    try:
        create_superuser()
        create_sample_data()
        print()
        print("✅ Setup tamamlandı!")
        print()
        print("Admin Panel: https://mavus-backend.onrender.com/admin/")
        print("Kullanıcı: admin")
        print("Şifre: admin123")
    except Exception as e:
        print(f"❌ Hata: {e}")
        import traceback
        traceback.print_exc()
