import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mavus_project.settings')
django.setup()

from products.models import Product, Category, ProductImage

# Tüm ürünleri ve kategorileri sil
print("Mevcut veriler temizleniyor...")
ProductImage.objects.all().delete()
Product.objects.all().delete()
Category.objects.all().delete()

print("\n" + "="*60)
print("YENİ KATEGORİLER OLUŞTURULUYOR")
print("="*60)

# Ana Kategoriler
bilezik = Category.objects.create(
    name="Bilezik",
    slug="bilezik",
    description="Zarif ve şık bilezik koleksiyonumuz"
)
print(f"✓ Ana Kategori: {bilezik.name}")

kolye = Category.objects.create(
    name="Kolye",
    slug="kolye",
    description="Benzersiz tasarım kolye modelleri"
)
print(f"✓ Ana Kategori: {kolye.name}")

yuzuk = Category.objects.create(
    name="Yüzük",
    slug="yuzuk",
    description="Özel günleriniz için yüzük seçenekleri"
)
print(f"✓ Ana Kategori: {yuzuk.name}")

kupe = Category.objects.create(
    name="Küpe",
    slug="kupe",
    description="Şıklığınızı tamamlayacak küpe modelleri"
)
print(f"✓ Ana Kategori: {kupe.name}")

print("\n" + "-"*60)
print("ALT KATEGORİLER OLUŞTURULUYOR")
print("-"*60)

# Bilezik Alt Kategorileri
altin_bilezik = Category.objects.create(
    name="Altın Bilezik",
    slug="altin-bilezik",
    description="Saf altın bilezik modelleri",
    parent=bilezik
)
print(f"  ↳ {bilezik.name} > {altin_bilezik.name}")

gumus_bilezik = Category.objects.create(
    name="Gümüş Bilezik",
    slug="gumus-bilezik",
    description="925 ayar gümüş bilezikler",
    parent=bilezik
)
print(f"  ↳ {bilezik.name} > {gumus_bilezik.name}")

pirlanta_bilezik = Category.objects.create(
    name="Pırlanta Bilezik",
    slug="pirlanta-bilezik",
    description="Pırlanta taşlı lüks bilezikler",
    parent=bilezik
)
print(f"  ↳ {bilezik.name} > {pirlanta_bilezik.name}")

# Kolye Alt Kategorileri
altin_kolye = Category.objects.create(
    name="Altın Kolye",
    slug="altin-kolye",
    description="Altın kolye modelleri",
    parent=kolye
)
print(f"  ↳ {kolye.name} > {altin_kolye.name}")

inci_kolye = Category.objects.create(
    name="İnci Kolye",
    slug="inci-kolye",
    description="Doğal inci kolyeler",
    parent=kolye
)
print(f"  ↳ {kolye.name} > {inci_kolye.name}")

tasli_kolye = Category.objects.create(
    name="Taşlı Kolye",
    slug="tasli-kolye",
    description="Değerli taş kolyeler",
    parent=kolye
)
print(f"  ↳ {kolye.name} > {tasli_kolye.name}")

# Yüzük Alt Kategorileri
nisan_yuzugu = Category.objects.create(
    name="Nişan Yüzüğü",
    slug="nisan-yuzugu",
    description="Özel gününüz için nişan yüzükleri",
    parent=yuzuk
)
print(f"  ↳ {yuzuk.name} > {nisan_yuzugu.name}")

alyans = Category.objects.create(
    name="Alyans",
    slug="alyans",
    description="Evlilik için alyans modelleri",
    parent=yuzuk
)
print(f"  ↳ {yuzuk.name} > {alyans.name}")

tasli_yuzuk = Category.objects.create(
    name="Taşlı Yüzük",
    slug="tasli-yuzuk",
    description="Değerli taşlı yüzükler",
    parent=yuzuk
)
print(f"  ↳ {yuzuk.name} > {tasli_yuzuk.name}")

# Küpe Alt Kategorileri
altin_kupe = Category.objects.create(
    name="Altın Küpe",
    slug="altin-kupe",
    description="Altın küpe modelleri",
    parent=kupe
)
print(f"  ↳ {kupe.name} > {altin_kupe.name}")

elmas_kupe = Category.objects.create(
    name="Elmas Küpe",
    slug="elmas-kupe",
    description="Elmas taşlı küpeler",
    parent=kupe
)
print(f"  ↳ {kupe.name} > {elmas_kupe.name}")

inci_kupe = Category.objects.create(
    name="İnci Küpe",
    slug="inci-kupe",
    description="İnci detaylı küpeler",
    parent=kupe
)
print(f"  ↳ {kupe.name} > {inci_kupe.name}")

print("\n" + "="*60)
print("ÖRNEK ÜRÜNLER EKLENIYOR")
print("="*60)

# Altın Bilezik Ürünleri
products_data = [
    # Altın Bilezikler
    {
        'name': 'Klasik Altın Bilezik',
        'category': altin_bilezik,
        'description': '22 ayar saf altından üretilmiş klasik bilezik modeli. Günlük kullanım için ideal.',
        'metal_type': 'gold',
        'karat': '22',
        'weight': 15.50,
        'price': 18500.00,
        'stock': 5,
        'is_featured': True,
        'is_best_seller': True
    },
    {
        'name': 'Hasır Altın Bilezik',
        'category': altin_bilezik,
        'description': 'Özel hasır işçiliği ile hazırlanmış zarif bilezik.',
        'metal_type': 'gold',
        'karat': '18',
        'weight': 12.30,
        'price': 14200.00,
        'stock': 8,
        'is_recommended': True
    },

    # Gümüş Bilezikler
    {
        'name': 'Mineli Gümüş Bilezik',
        'category': gumus_bilezik,
        'description': '925 ayar gümüşten yapılmış, el işi mine detaylı bilezik.',
        'metal_type': 'silver',
        'karat': '',
        'weight': 18.00,
        'price': 2500.00,
        'stock': 12,
        'is_featured': True
    },
    {
        'name': 'Telkari Gümüş Bilezik',
        'category': gumus_bilezik,
        'description': 'Geleneksel telkari işçiliği ile özel olarak hazırlanmıştır.',
        'metal_type': 'silver',
        'karat': '',
        'weight': 20.00,
        'price': 3200.00,
        'stock': 6,
        'is_best_seller': True
    },

    # Pırlanta Bilezikler
    {
        'name': 'Lüks Pırlanta Bilezik',
        'category': pirlanta_bilezik,
        'description': '18 ayar beyaz altın üzerine toplam 2.5 karat pırlanta.',
        'metal_type': 'white_gold',
        'karat': '18',
        'weight': 25.00,
        'price': 85000.00,
        'stock': 2,
        'is_featured': True,
        'is_recommended': True
    },

    # Altın Kolyeler
    {
        'name': 'Kalp Kolye',
        'category': altin_kolye,
        'description': '14 ayar altın kalp uçlu kolye, romantik tasarım.',
        'metal_type': 'gold',
        'karat': '14',
        'weight': 3.50,
        'price': 3800.00,
        'stock': 15,
        'is_best_seller': True,
        'is_recommended': True
    },
    {
        'name': 'Zincir Kolye',
        'category': altin_kolye,
        'description': '22 ayar altın ince zincir kolye.',
        'metal_type': 'gold',
        'karat': '22',
        'weight': 5.20,
        'price': 6200.00,
        'stock': 10,
        'is_featured': True
    },

    # İnci Kolyeler
    {
        'name': 'Doğal İnci Kolye',
        'category': inci_kolye,
        'description': 'Güney denizi incisi ile hazırlanmış özel kolye.',
        'metal_type': 'white_gold',
        'karat': '14',
        'weight': 8.00,
        'price': 12500.00,
        'stock': 4,
        'is_featured': True,
        'is_best_seller': True
    },

    # Taşlı Kolyeler
    {
        'name': 'Yakut Taşlı Kolye',
        'category': tasli_kolye,
        'description': 'Doğal yakut taşı ve rose altın kombinasyonu.',
        'metal_type': 'rose_gold',
        'karat': '18',
        'weight': 6.50,
        'price': 22000.00,
        'stock': 3,
        'is_recommended': True
    },

    # Nişan Yüzükleri
    {
        'name': 'Tek Taş Nişan Yüzüğü',
        'category': nisan_yuzugu,
        'description': '1 karat pırlanta tek taş, 18 ayar beyaz altın.',
        'metal_type': 'white_gold',
        'karat': '18',
        'weight': 4.50,
        'price': 45000.00,
        'stock': 5,
        'is_featured': True,
        'is_best_seller': True,
        'is_recommended': True
    },
    {
        'name': 'Regal Nişan Yüzüğü',
        'category': nisan_yuzugu,
        'description': 'Merkez 0.75 karat ve etrafı taşlı özel tasarım.',
        'metal_type': 'white_gold',
        'karat': '18',
        'weight': 5.20,
        'price': 38000.00,
        'stock': 3,
        'is_featured': True
    },

    # Alyanslar
    {
        'name': 'Klasik Alyans Çifti',
        'category': alyans,
        'description': '14 ayar sarı altın düz alyans modeli.',
        'metal_type': 'gold',
        'karat': '14',
        'weight': 8.00,
        'price': 9200.00,
        'stock': 10,
        'is_best_seller': True
    },
    {
        'name': 'Taşlı Alyans Çifti',
        'category': alyans,
        'description': 'Kadın halkasında pırlanta detaylı alyans.',
        'metal_type': 'white_gold',
        'karat': '14',
        'weight': 9.50,
        'price': 15000.00,
        'stock': 6,
        'is_recommended': True
    },

    # Taşlı Yüzükler
    {
        'name': 'Zümrüt Yüzük',
        'category': tasli_yuzuk,
        'description': 'Kolombiya zümrütü ve pırlanta detaylı lüks yüzük.',
        'metal_type': 'gold',
        'karat': '18',
        'weight': 6.80,
        'price': 32000.00,
        'stock': 2,
        'is_featured': True
    },

    # Altın Küpeler
    {
        'name': 'Halka Küpe',
        'category': altin_kupe,
        'description': '14 ayar altın klasik halka küpe.',
        'metal_type': 'gold',
        'karat': '14',
        'weight': 4.00,
        'price': 4500.00,
        'stock': 20,
        'is_best_seller': True
    },
    {
        'name': 'Sallantılı Küpe',
        'category': altin_kupe,
        'description': '18 ayar rose altın sallantılı model.',
        'metal_type': 'rose_gold',
        'karat': '18',
        'weight': 5.50,
        'price': 6800.00,
        'stock': 8,
        'is_recommended': True
    },

    # Elmas Küpeler
    {
        'name': 'Elmas Tektaş Küpe',
        'category': elmas_kupe,
        'description': 'Toplam 1 karat elmas, beyaz altın.',
        'metal_type': 'white_gold',
        'karat': '18',
        'weight': 3.20,
        'price': 28000.00,
        'stock': 4,
        'is_featured': True,
        'is_best_seller': True
    },

    # İnci Küpeler
    {
        'name': 'İnci Damla Küpe',
        'category': inci_kupe,
        'description': 'Doğal inci damla küpe, zarif tasarım.',
        'metal_type': 'white_gold',
        'karat': '14',
        'weight': 4.50,
        'price': 8500.00,
        'stock': 7,
        'is_recommended': True
    },
]

for i, product_data in enumerate(products_data, 1):
    product = Product.objects.create(
        name=product_data['name'],
        slug=f"{product_data['category'].slug}-{i}",
        category=product_data['category'],
        description=product_data['description'],
        metal_type=product_data['metal_type'],
        karat=product_data['karat'],
        weight=product_data['weight'],
        price=product_data['price'],
        stock=product_data['stock'],
        is_available=True,
        is_featured=product_data.get('is_featured', False),
        is_best_seller=product_data.get('is_best_seller', False),
        is_recommended=product_data.get('is_recommended', False)
    )
    status = []
    if product.is_featured:
        status.append("Öne Çıkan")
    if product.is_best_seller:
        status.append("Çok Satan")
    if product.is_recommended:
        status.append("Önerilen")

    status_str = f" [{', '.join(status)}]" if status else ""
    print(f"✓ {product.category.parent.name if product.category.parent else product.category.name} > {product.category.name}: {product.name}{status_str}")

print("\n" + "="*60)
print("ÖZET")
print("="*60)
print(f"Toplam Kategori: {Category.objects.count()}")
print(f"  - Ana Kategoriler: {Category.objects.filter(parent__isnull=True).count()}")
print(f"  - Alt Kategoriler: {Category.objects.filter(parent__isnull=False).count()}")
print(f"Toplam Ürün: {Product.objects.count()}")
print(f"  - Öne Çıkan: {Product.objects.filter(is_featured=True).count()}")
print(f"  - Çok Satan: {Product.objects.filter(is_best_seller=True).count()}")
print(f"  - Önerilen: {Product.objects.filter(is_recommended=True).count()}")
print("="*60)
print("✅ Veriler başarıyla eklendi!")
