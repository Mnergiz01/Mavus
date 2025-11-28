from rest_framework import serializers
from .models import Category, Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'alt_text']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description']


class ProductListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    metal_type_display = serializers.CharField(source='get_metal_type_display', read_only=True)
    karat_display = serializers.CharField(source='get_karat_display', read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'category', 'description',
            'metal_type', 'metal_type_display', 'karat', 'karat_display',
            'weight', 'price', 'stock', 'image', 'is_featured', 'created_at'
        ]


class ProductDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    metal_type_display = serializers.CharField(source='get_metal_type_display', read_only=True)
    karat_display = serializers.CharField(source='get_karat_display', read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'category', 'description',
            'metal_type', 'metal_type_display', 'karat', 'karat_display',
            'weight', 'price', 'stock', 'image', 'images',
            'is_available', 'is_featured', 'created_at', 'updated_at'
        ]
