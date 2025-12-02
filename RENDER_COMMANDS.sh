#!/bin/bash
# Render Shell'de çalıştırılacak komutlar
# https://dashboard.render.com/ → Backend Service → Shell

echo "🚀 Production Database Güncelleme Başlıyor..."
echo ""

# 1. Migration
echo "📦 Step 1: Migration çalıştırılıyor..."
python manage.py migrate
echo "✅ Migration tamamlandı"
echo ""

# 2. Eski verileri temizle
echo "🗑️  Step 2: Eski veriler temizleniyor..."
python manage.py shell << 'PYTHON_EOF'
from products.models import Product, Category, ProductImage
deleted_products = Product.objects.all().delete()
deleted_categories = Category.objects.all().delete()
deleted_images = ProductImage.objects.all().delete()
print(f"✅ Silindi - Products: {deleted_products[0]}, Categories: {deleted_categories[0]}, Images: {deleted_images[0]}")
PYTHON_EOF
echo ""

# 3. Yeni verileri yükle
echo "📥 Step 3: Yeni veriler yükleniyor..."
python manage.py create_sample_data
echo ""

# 4. Kontrol
echo "🔍 Step 4: Veriler kontrol ediliyor..."
python manage.py shell << 'PYTHON_EOF'
from products.models import Product, Category
cat_count = Category.objects.count()
prod_count = Product.objects.count()
parent_cats = Category.objects.filter(parent=None)

print(f"📊 Toplam Kategori: {cat_count}")
print(f"📊 Toplam Ürün: {prod_count}")
print(f"📊 Ana Kategoriler: {parent_cats.count()}")
print("")
print("📝 Ana Kategoriler:")
for cat in parent_cats:
    children = cat.children.count()
    print(f"  - {cat.name} ({children} alt kategori)")
PYTHON_EOF
echo ""

echo "✅ Güncelleme tamamlandı!"
echo "🌐 Test: https://mavus-backend.onrender.com/api/categories/"
