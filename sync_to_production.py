#!/usr/bin/env python
"""
Local veritabanındaki ürünleri Render production veritabanına aktarır

Kullanım:
    python sync_to_production.py "postgresql://user:pass@host/db"
"""
import os
import sys
import django

if len(sys.argv) < 2:
    print("❌ Kullanım: python sync_to_production.py 'DATABASE_URL'")
    print("\nÖrnek:")
    print("  python sync_to_production.py 'postgresql://mavus_user:XXX@dpg-xxx.oregon-postgres.render.com/mavus_production'")
    sys.exit(1)

RENDER_DATABASE_URL = sys.argv[1]

# Django setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mavus_project.settings')
os.environ['DATABASE_URL'] = RENDER_DATABASE_URL

django.setup()

from django.core.management import call_command
from products.models import Category, Product, ProductImage

print("\n🔄 Production veritabanına bağlanılıyor...")

# Mevcut verileri temizle
print("\n⚠️  Production'daki mevcut ürünler temizleniyor...")
Product.objects.all().delete()
Category.objects.all().delete()
print("✅ Mevcut veriler temizlendi")

# JSON dosyasından verileri yükle
print("\n📦 Local veriler production'a aktarılıyor...")
try:
    call_command('loaddata', 'products_backup.json')
    print("\n✅ Veriler başarıyla aktarıldı!")

    # İstatistikler
    cat_count = Category.objects.count()
    prod_count = Product.objects.count()
    print(f"\n📊 İstatistikler:")
    print(f"   - Kategoriler: {cat_count}")
    print(f"   - Ürünler: {prod_count}")

except Exception as e:
    print(f"\n❌ Hata oluştu: {e}")
    sys.exit(1)
