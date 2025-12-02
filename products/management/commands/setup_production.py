from django.core.management.base import BaseCommand
from products.models import Category, Product, ProductImage
from decimal import Decimal


class Command(BaseCommand):
    help = 'Setup production database with sample data (idempotent)'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing data before loading',
        )

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('🚀 Production Setup Starting...'))

        # Clear if requested
        if options['clear']:
            self.stdout.write(self.style.WARNING('🗑️  Clearing existing data...'))
            Product.objects.all().delete()
            Category.objects.all().delete()
            ProductImage.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('✅ Data cleared'))

        # Check if data already exists
        if Category.objects.exists():
            self.stdout.write(self.style.WARNING('⚠️  Categories already exist. Use --clear to reset.'))
            return

        # Run sample data creation
        from .create_sample_data import Command as SampleDataCommand
        sample_cmd = SampleDataCommand()
        sample_cmd.handle()

        self.stdout.write(self.style.SUCCESS('✅ Production setup complete!'))
