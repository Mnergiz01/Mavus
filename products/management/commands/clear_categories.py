from django.core.management.base import BaseCommand
from products.models import Category


class Command(BaseCommand):
    help = 'Tüm kategorileri veritabanından siler'

    def handle(self, *args, **kwargs):
        count = Category.objects.count()
        
        if count == 0:
            self.stdout.write(
                self.style.WARNING('Veritabanında kategori bulunamadı.')
            )
            return
        
        self.stdout.write(f'Toplam {count} kategori siliniyor...')
        Category.objects.all().delete()
        
        self.stdout.write(
            self.style.SUCCESS(f'✓ {count} kategori başarıyla silindi!')
        )
