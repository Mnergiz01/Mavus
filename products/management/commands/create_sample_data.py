from django.core.management.base import BaseCommand
from products.models import Category, Product
from decimal import Decimal


class Command(BaseCommand):
    help = 'Create sample categories and products for Mawuş Kuyumculuk'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Creating sample data...'))

        # Ana Kategoriler ve Alt Kategoriler
        categories_data = {
            'Yüzük': {
                'image': 'https://images.unsplash.com/photo-1605100804763-247f67b3557e?w=400&h=400&fit=crop',
                'subcategories': [
                    {'name': 'Tek Taş Yüzük', 'image': 'https://images.unsplash.com/photo-1611591437281-460bfbe1220a?w=400&h=400&fit=crop'},
                    {'name': 'Nişan Yüzüğü', 'image': 'https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?w=400&h=400&fit=crop'},
                    {'name': 'Alyans', 'image': 'https://images.unsplash.com/photo-1606800052052-a08af7148866?w=400&h=400&fit=crop'},
                    {'name': 'Çeyrek Yüzük', 'image': 'https://images.unsplash.com/photo-1617038260897-41a1f14a8ca0?w=400&h=400&fit=crop'},
                    {'name': 'Pırlanta Yüzük', 'image': 'https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?w=400&h=400&fit=crop'},
                ]
            },
            'Kolye': {
                'image': 'https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?w=400&h=400&fit=crop',
                'subcategories': [
                    {'name': 'Altın Kolye', 'image': 'https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?w=400&h=400&fit=crop'},
                    {'name': 'Pırlanta Kolye', 'image': 'https://images.unsplash.com/photo-1603561591411-07134e71a2a9?w=400&h=400&fit=crop'},
                    {'name': 'İsimli Kolye', 'image': 'https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?w=400&h=400&fit=crop'},
                    {'name': 'Tuğralı Kolye', 'image': 'https://images.unsplash.com/photo-1611085583191-a3b181a88401?w=400&h=400&fit=crop'},
                    {'name': 'Şans Kolyesi', 'image': 'https://images.unsplash.com/photo-1596944924591-4b15d4e2e5b8?w=400&h=400&fit=crop'},
                ]
            },
            'Bileklik': {
                'image': 'https://images.unsplash.com/photo-1611591437281-460bfbe1220a?w=400&h=400&fit=crop',
                'subcategories': [
                    {'name': 'Altın Bileklik', 'image': 'https://images.unsplash.com/photo-1611591437281-460bfbe1220a?w=400&h=400&fit=crop'},
                    {'name': 'Kelepçe', 'image': 'https://images.unsplash.com/photo-1573408301185-9146fe634ad0?w=400&h=400&fit=crop'},
                    {'name': 'Pırlanta Bileklik', 'image': 'https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?w=400&h=400&fit=crop'},
                    {'name': 'İsimli Bileklik', 'image': 'https://images.unsplash.com/photo-1611085583191-a3b181a88401?w=400&h=400&fit=crop'},
                    {'name': 'Zincir Bileklik', 'image': 'https://images.unsplash.com/photo-1611591437281-460bfbe1220a?w=400&h=400&fit=crop'},
                ]
            },
            'Küpe': {
                'image': 'https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?w=400&h=400&fit=crop',
                'subcategories': [
                    {'name': 'Halka Küpe', 'image': 'https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?w=400&h=400&fit=crop'},
                    {'name': 'Pırlanta Küpe', 'image': 'https://images.unsplash.com/photo-1617038260897-41a1f14a8ca0?w=400&h=400&fit=crop'},
                    {'name': 'Sallantılı Küpe', 'image': 'https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?w=400&h=400&fit=crop'},
                    {'name': 'Tek Taş Küpe', 'image': 'https://images.unsplash.com/photo-1603561591411-07134e71a2a9?w=400&h=400&fit=crop'},
                    {'name': 'Mini Küpe', 'image': 'https://images.unsplash.com/photo-1611085583191-a3b181a88401?w=400&h=400&fit=crop'},
                ]
            },
            'Set': {
                'image': 'https://images.unsplash.com/photo-1603561591411-07134e71a2a9?w=400&h=400&fit=crop',
                'subcategories': [
                    {'name': 'Altın Set', 'image': 'https://images.unsplash.com/photo-1611085583191-a3b181a88401?w=400&h=400&fit=crop'},
                    {'name': 'Pırlanta Set', 'image': 'https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?w=400&h=400&fit=crop'},
                    {'name': 'Gelin Seti', 'image': 'https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?w=400&h=400&fit=crop'},
                    {'name': 'Üçlü Set', 'image': 'https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?w=400&h=400&fit=crop'},
                ]
            },
        }

        # Kategorileri oluştur
        created_categories = {}

        for parent_name, parent_data in categories_data.items():
            # Ana kategoriyi oluştur
            parent_cat, created = Category.objects.get_or_create(
                name=parent_name,
                defaults={
                    'description': f'{parent_name} kategorisi - Mawuş Kuyumculuk',
                    'image': parent_data['image'],
                }
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'✓ Ana kategori oluşturuldu: {parent_name}'))
            else:
                self.stdout.write(self.style.WARNING(f'○ Ana kategori mevcut: {parent_name}'))

            created_categories[parent_name] = {'parent': parent_cat, 'children': []}

            # Alt kategorileri oluştur
            for sub_data in parent_data['subcategories']:
                sub_cat, created = Category.objects.get_or_create(
                    name=sub_data['name'],
                    parent=parent_cat,
                    defaults={
                        'description': f'{sub_data["name"]} - {parent_name} kategorisi',
                        'image': sub_data['image'],
                    }
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f'  ✓ Alt kategori oluşturuldu: {sub_data["name"]}'))
                else:
                    self.stdout.write(self.style.WARNING(f'  ○ Alt kategori mevcut: {sub_data["name"]}'))

                created_categories[parent_name]['children'].append(sub_cat)

        self.stdout.write(self.style.SUCCESS('\n--- Kategoriler oluşturuldu ---\n'))

        # Örnek ürünler
        sample_products = [
            # Yüzükler
            {
                'name': '14 Ayar Altın Tek Taş Pırlanta Yüzük',
                'description': 'Şık ve zarif tasarımı ile göz alıcı 14 ayar altın tek taş pırlanta yüzük.',
                'category': 'Tek Taş Yüzük',
                'metal_type': 'gold',
                'karat': 14,
                'weight': Decimal('3.5'),
                'stock_code': 'YZ-001',
                'image': 'https://images.unsplash.com/photo-1605100804763-247f67b3557e?w=800&h=800&fit=crop',
                'is_featured': True,
                'is_best_seller': True,
            },
            {
                'name': '18 Ayar Altın Nişan Yüzüğü',
                'description': 'Özel günleriniz için tasarlanmış 18 ayar altın nişan yüzüğü.',
                'category': 'Nişan Yüzüğü',
                'metal_type': 'gold',
                'karat': 18,
                'weight': Decimal('4.2'),
                'stock_code': 'YZ-002',
                'image': 'https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?w=800&h=800&fit=crop',
                'is_featured': True,
                'is_recommended': True,
            },
            {
                'name': '14 Ayar Altın Alyans Çifti',
                'description': 'Sade ve şık tasarımı ile alyans çifti.',
                'category': 'Alyans',
                'metal_type': 'gold',
                'karat': 14,
                'weight': Decimal('6.8'),
                'stock_code': 'YZ-003',
                'image': 'https://images.unsplash.com/photo-1606800052052-a08af7148866?w=800&h=800&fit=crop',
                'is_best_seller': True,
            },
            {
                'name': '22 Ayar Altın Çeyrek Yüzük',
                'description': 'Geleneksel çeyrek altın yüzük.',
                'category': 'Çeyrek Yüzük',
                'metal_type': 'gold',
                'karat': 22,
                'weight': Decimal('5.5'),
                'stock_code': 'YZ-004',
                'image': 'https://images.unsplash.com/photo-1617038260897-41a1f14a8ca0?w=800&h=800&fit=crop',
                'is_recommended': True,
            },

            # Kolyeler
            {
                'name': '14 Ayar Altın Kalp Kolye',
                'description': 'Sevdiklerinize özel kalp tasarımlı altın kolye.',
                'category': 'Altın Kolye',
                'metal_type': 'gold',
                'karat': 14,
                'weight': Decimal('2.8'),
                'stock_code': 'KL-001',
                'image': 'https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?w=800&h=800&fit=crop',
                'is_featured': True,
            },
            {
                'name': 'Pırlanta Taşlı Yıldız Kolye',
                'description': 'Işıltılı pırlanta taşlarla süslenmiş yıldız kolye.',
                'category': 'Pırlanta Kolye',
                'metal_type': 'white_gold',
                'karat': 14,
                'weight': Decimal('3.2'),
                'stock_code': 'KL-002',
                'image': 'https://images.unsplash.com/photo-1603561591411-07134e71a2a9?w=800&h=800&fit=crop',
                'is_featured': True,
                'is_best_seller': True,
            },
            {
                'name': '18 Ayar İsim Yazılı Kolye',
                'description': 'Kişiye özel isim yazılı altın kolye.',
                'category': 'İsimli Kolye',
                'metal_type': 'rose_gold',
                'karat': 18,
                'weight': Decimal('2.5'),
                'stock_code': 'KL-003',
                'image': 'https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?w=800&h=800&fit=crop',
                'is_recommended': True,
            },

            # Bileklikler
            {
                'name': '14 Ayar Altın Zincir Bileklik',
                'description': 'Zarif ve ince tasarımlı altın zincir bileklik.',
                'category': 'Zincir Bileklik',
                'metal_type': 'gold',
                'karat': 14,
                'weight': Decimal('4.5'),
                'stock_code': 'BL-001',
                'image': 'https://images.unsplash.com/photo-1611591437281-460bfbe1220a?w=800&h=800&fit=crop',
                'is_best_seller': True,
            },
            {
                'name': '18 Ayar Altın Kelepçe',
                'description': 'Klasik ve şık altın kelepçe.',
                'category': 'Kelepçe',
                'metal_type': 'gold',
                'karat': 18,
                'weight': Decimal('12.5'),
                'stock_code': 'BL-002',
                'image': 'https://images.unsplash.com/photo-1573408301185-9146fe634ad0?w=800&h=800&fit=crop',
                'is_featured': True,
            },
            {
                'name': 'Pırlanta Taşlı Bileklik',
                'description': 'Pırlanta taşlarla süslenmiş lüks bileklik.',
                'category': 'Pırlanta Bileklik',
                'metal_type': 'white_gold',
                'karat': 14,
                'weight': Decimal('8.2'),
                'stock_code': 'BL-003',
                'image': 'https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?w=800&h=800&fit=crop',
                'is_featured': True,
                'is_recommended': True,
            },

            # Küpeler
            {
                'name': '14 Ayar Altın Halka Küpe',
                'description': 'Klasik halka küpe modeli.',
                'category': 'Halka Küpe',
                'metal_type': 'gold',
                'karat': 14,
                'weight': Decimal('2.8'),
                'stock_code': 'KP-001',
                'image': 'https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?w=800&h=800&fit=crop',
                'is_best_seller': True,
            },
            {
                'name': 'Pırlanta Tek Taş Küpe',
                'description': 'Şık ve zarif pırlanta tek taş küpe.',
                'category': 'Tek Taş Küpe',
                'metal_type': 'white_gold',
                'karat': 14,
                'weight': Decimal('1.8'),
                'stock_code': 'KP-002',
                'image': 'https://images.unsplash.com/photo-1603561591411-07134e71a2a9?w=800&h=800&fit=crop',
                'is_featured': True,
                'is_best_seller': True,
            },
            {
                'name': '18 Ayar Sallantılı Küpe',
                'description': 'Zarif sallantılı tasarım küpe.',
                'category': 'Sallantılı Küpe',
                'metal_type': 'rose_gold',
                'karat': 18,
                'weight': Decimal('3.5'),
                'stock_code': 'KP-003',
                'image': 'https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?w=800&h=800&fit=crop',
                'is_recommended': True,
            },

            # Setler
            {
                'name': '14 Ayar Gelin Seti (3\'lü)',
                'description': 'Özel gününüz için tasarlanmış gelin seti - Kolye, Küpe, Bileklik.',
                'category': 'Gelin Seti',
                'metal_type': 'gold',
                'karat': 14,
                'weight': Decimal('15.5'),
                'stock_code': 'ST-001',
                'image': 'https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?w=800&h=800&fit=crop',
                'is_featured': True,
                'is_best_seller': True,
            },
            {
                'name': 'Pırlanta Taşlı Lüks Set',
                'description': 'Pırlanta taşlarla süslenmiş lüks set.',
                'category': 'Pırlanta Set',
                'metal_type': 'white_gold',
                'karat': 14,
                'weight': Decimal('18.2'),
                'stock_code': 'ST-002',
                'image': 'https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?w=800&h=800&fit=crop',
                'is_featured': True,
            },
        ]

        # Ürünleri oluştur
        created_count = 0
        for product_data in sample_products:
            category_name = product_data.pop('category')

            # Kategoriyi bul
            category = None
            for parent_name, cat_data in created_categories.items():
                for child_cat in cat_data['children']:
                    if child_cat.name == category_name:
                        category = child_cat
                        break
                if category:
                    break

            if not category:
                self.stdout.write(self.style.ERROR(f'✗ Kategori bulunamadı: {category_name}'))
                continue

            # Ürünü oluştur
            product, created = Product.objects.get_or_create(
                stock_code=product_data['stock_code'],
                defaults={
                    **product_data,
                    'category': category,
                    'is_available': True,
                    'price': Decimal('0.00'),  # Fiyat admin panelden güncellenecek
                }
            )

            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f'✓ Ürün oluşturuldu: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'○ Ürün mevcut: {product.name}'))

        self.stdout.write(self.style.SUCCESS(f'\n✅ Toplam {created_count} yeni ürün oluşturuldu!'))
        self.stdout.write(self.style.SUCCESS('✅ Örnek veriler başarıyla yüklendi!'))
