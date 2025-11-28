from django.contrib import admin
from .models import Category, Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ('image', 'alt_text')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('created_at',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'metal_type', 'karat', 'weight', 'price', 'stock', 'is_available', 'is_featured', 'created_at')
    list_filter = ('category', 'metal_type', 'karat', 'is_available', 'is_featured', 'created_at')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('is_available', 'is_featured', 'price', 'stock')
    inlines = [ProductImageInline]

    fieldsets = (
        ('Genel Bilgiler', {
            'fields': ('name', 'slug', 'category', 'description')
        }),
        ('Ürün Özellikleri', {
            'fields': ('metal_type', 'karat', 'weight')
        }),
        ('Fiyat ve Stok', {
            'fields': ('price', 'stock')
        }),
        ('Resim', {
            'fields': ('image',)
        }),
        ('Durum', {
            'fields': ('is_available', 'is_featured')
        }),
    )


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'alt_text', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('product__name', 'alt_text')
