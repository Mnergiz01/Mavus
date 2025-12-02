# 🚀 Production Database Güncelleme Rehberi

## ❗ SORUN

Vercel'deki sitenizde dropdown ve ürünler **farklı** görünüyor çünkü:
- **Lokal:** Yeni kategoriler (Yüzük, Kolye, Bileklik, Küpe, Set) + 15 ürün ✅
- **Production (Render):** Eski veriler (3 kategori + 4 ürün) ❌

## ✅ ÇÖZÜM: Production'ı Güncelle

### Yöntem 1: Render Dashboard (Önerilen)

#### Adım 1: Migration Çalıştır

1. [Render Dashboard](https://dashboard.render.com/) → Backend servisiniz
2. **Shell** sekmesine git
3. Şu komutları çalıştır:

```bash
python manage.py migrate
```

#### Adım 2: Eski Verileri Temizle (Opsiyonel)

**DİKKAT:** Bu komut tüm ürün ve kategorileri siler!

```bash
python manage.py shell
```

Shell açıldığında:

```python
from products.models import Product, Category, ProductImage
Product.objects.all().delete()
Category.objects.all().delete()
ProductImage.objects.all().delete()
exit()
```

#### Adım 3: Yeni Verileri Yükle

```bash
python manage.py create_sample_data
```

Bu komut:
- ✅ 5 ana kategori (Yüzük, Kolye, Bileklik, Küpe, Set)
- ✅ 24 alt kategori
- ✅ 15 örnek ürün
- ✅ Profesyonel fotoğraflar (Unsplash URL'leri)

#### Adım 4: Restart

Render Dashboard → **Manual Deploy** → **Deploy latest commit**

---

### Yöntem 2: Lokal Database'den Export (İleri Seviye)

#### 1. Lokal Data Export

```bash
# Lokal veritabanından data export et
python manage.py dumpdata products --natural-foreign --natural-primary -e contenttypes -e auth.Permission --indent 2 > products_data.json
```

#### 2. Production'a Upload

Bu dosyayı Render'a yükleyip:

```bash
# Render shell'de
python manage.py loaddata products_data.json
```

**SORUN:** Bu yöntem karmaşık, ImageField path'leri çalışmayabilir.

---

## 🎯 Önerilen Yol: create_sample_data Kullan

### Neden?

✅ Kolay ve hızlı
✅ URL-based resimler (çalışır garantili)
✅ Tutarlı veriler
✅ Hemen kullanıma hazır

### Nasıl?

1. Render Dashboard → Shell
2. Komutlar:

```bash
# Migration
python manage.py migrate

# Eski verileri temizle (isteğe bağlı)
python manage.py shell -c "from products.models import *; Product.objects.all().delete(); Category.objects.all().delete()"

# Yeni verileri yükle
python manage.py create_sample_data

# Kontrol et
python manage.py shell -c "from products.models import *; print(f'Categories: {Category.objects.count()}, Products: {Product.objects.count()}')"
```

Çıktı şöyle olmalı:
```
Categories: 29, Products: 15
```

---

## ✨ Alternatif: Manuel Ürün Ekleme

Eğer kendi ürünlerinizi eklemek istiyorsanız:

1. Admin Panel: `https://mavus-backend.onrender.com/admin/`
2. Products → Add Product
3. Resim için **URL** kullanın (örn: Unsplash, kendi CDN)
4. Kategorileri manuel oluşturun

---

## 🔍 Test

Güncelleme sonrası kontrol:

```bash
# Backend test
curl https://mavus-backend.onrender.com/api/categories/

# Kategori sayısı 5 olmalı (Yüzük, Kolye, Bileklik, Küpe, Set)
```

## 📝 Önemli Notlar

1. **Migration:** Zaten yapıldı (0006), tekrar çalıştırılabilir
2. **Resimler:** URL kullanıyoruz, upload gerekmez
3. **Backup:** Render otomatik backup alıyor
4. **Restart:** Migration sonrası otomatik restart olur

---

## 🎯 Sonraki Adımlar

1. ✅ Render'da migration çalıştır
2. ✅ Örnek verileri yükle (create_sample_data)
3. ✅ Vercel'i test et: https://mavus-g6p22.vercel.app
4. ✅ Dropdown ve ürünlerin göründüğünü kontrol et

**Artık lokal ile production aynı olacak!** 🎉
