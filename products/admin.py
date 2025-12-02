from django.contrib import admin
from django.contrib import messages
from django.core.management import call_command
from .models import Category, Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ('image', 'alt_text', 'is_video', 'order')


def setup_production_data(modeladmin, request, queryset):
    """Admin action to setup production database with sample data"""
    try:
        # Clear existing data
        Product.objects.all().delete()
        Category.objects.all().delete()
        ProductImage.objects.all().delete()

        # Load sample data
        call_command('create_sample_data')

        messages.success(request, '✅ Production data successfully updated! 29 categories and 15 products created.')
    except Exception as e:
        messages.error(request, f'❌ Error updating production data: {str(e)}')

setup_production_data.short_description = "🚀 Update Production Database (Clear & Load Sample Data)"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'slug', 'created_at')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('parent', 'created_at')
    autocomplete_fields = ['parent']
    actions = [setup_production_data]

    fieldsets = (
        ('Genel Bilgiler', {
            'fields': ('name', 'slug', 'parent', 'description')
        }),
        ('Görsel', {
            'fields': ('image',)
        }),
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'stock_code', 'category', 'metal_type', 'karat', 'weight', 'price', 'is_available', 'is_featured', 'is_best_seller', 'is_recommended', 'created_at')
    list_filter = ('category', 'metal_type', 'karat', 'is_available', 'is_featured', 'is_best_seller', 'is_recommended', 'created_at')
    search_fields = ('name', 'description', 'stock_code')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('is_available', 'is_featured', 'is_best_seller', 'is_recommended')
    inlines = [ProductImageInline]

    fieldsets = (
        ('Genel Bilgiler', {
            'fields': ('name', 'slug', 'category', 'description')
        }),
        ('Ürün Özellikleri', {
            'fields': ('metal_type', 'karat', 'weight')
        }),
        ('Fiyat ve Stok', {
            'fields': ('price', 'stock_code')
        }),
        ('Resim', {
            'fields': ('image',)
        }),
        ('Durum', {
            'fields': ('is_available', 'is_featured', 'is_best_seller', 'is_recommended')
        }),
    )


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'alt_text', 'is_video', 'order', 'created_at')
    list_filter = ('is_video', 'created_at')
    search_fields = ('product__name', 'alt_text')
    list_editable = ('order',)
