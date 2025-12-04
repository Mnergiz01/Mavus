from django.core.management.base import BaseCommand
from products.models import Category
from django.utils.text import slugify


class Command(BaseCommand):
    help = 'Kategori hiyerarşisini veritabanına ekler'

    def handle(self, *args, **kwargs):
        self.stdout.write('Kategoriler ekleniyor...')

        # Kategori yapısı
        categories_structure = {
            'Bilezik': [
                'Hediyelik (3-8 gr)',
                'Chanel',
                'Kıvırcık',
                'Adana Burması'
            ],
            'Bileklik': [
                '14 Ayar',
                '22 Ayar'
            ],
            'Kolye': [
                '14 Ayar',
                '22 Ayar'
            ],
            'Kolye Ucu': [
                '14 Ayar',
                '22 Ayar'
            ],
            'Küpe': [
                '14 Ayar',
                '22 Ayar'
            ],
            'Yüzük': [
                '14 Ayar Baget',
                '14 Ayar Tektaş',
                '14 Ayar Çıtır',
                '22 Ayar Baget',
                '22 Ayar Tektaş',
                '22 Ayar Yüzük'
            ],
            'Set': [
                '14 Ayar',
                '22 Ayar'
            ]
        }

        # Her ana kategori için
        for parent_name, children_names in categories_structure.items():
            # Ana kategoriyi oluştur veya getir
            parent, created = Category.objects.get_or_create(
                name=parent_name,
                defaults={
                    'slug': slugify(parent_name, allow_unicode=True),
                    'description': f'{parent_name} kategorisi'
                }
            )
            
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'✓ Ana kategori oluşturuldu: {parent_name}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'○ Ana kategori zaten mevcut: {parent_name}')
                )

            # Alt kategorileri oluştur
            for child_name in children_names:
                child, created = Category.objects.get_or_create(
                    name=child_name,
                    parent=parent,
                    defaults={
                        'slug': slugify(f'{parent_name}-{child_name}', allow_unicode=True),
                        'description': f'{parent_name} - {child_name}'
                    }
                )
                
                if created:
                    self.stdout.write(
                        self.style.SUCCESS(f'  ✓ Alt kategori oluşturuldu: {child_name}')
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(f'  ○ Alt kategori zaten mevcut: {child_name}')
                    )

        self.stdout.write(
            self.style.SUCCESS('\n✓ Tüm kategoriler başarıyla eklendi!')
        )
        
        # Kategori özetini göster
        total_categories = Category.objects.count()
        parent_categories = Category.objects.filter(parent__isnull=True).count()
        child_categories = Category.objects.filter(parent__isnull=False).count()
        
        self.stdout.write(
            self.style.SUCCESS(
                f'\nToplam: {total_categories} kategori ({parent_categories} ana, {child_categories} alt)'
            )
        )
