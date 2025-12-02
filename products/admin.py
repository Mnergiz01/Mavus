from django.contrib import admin
from .models import Category, Product, ProductImage, ProductVideo


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ('image', 'alt_text', 'order')


class ProductVideoInline(admin.TabularInline):
    model = ProductVideo
    extra = 1
    fields = ('video', 'thumbnail', 'title', 'order')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'slug', 'created_at')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('parent', 'created_at')
    autocomplete_fields = ['parent']

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
    inlines = [ProductImageInline, ProductVideoInline]

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
    list_display = ('product', 'alt_text', 'order', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('product__name', 'alt_text')
    list_editable = ('order',)


@admin.register(ProductVideo)
class ProductVideoAdmin(admin.ModelAdmin):
    list_display = ('product', 'title', 'order', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('product__name', 'title')
    list_editable = ('order',)
