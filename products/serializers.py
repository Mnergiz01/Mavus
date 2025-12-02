from rest_framework import serializers
from .models import Category, Product, ProductImage, ProductVideo


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'alt_text', 'order']


class ProductVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVideo
        fields = ['id', 'video', 'thumbnail', 'title', 'order']


class CategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description', 'parent', 'image', 'children']

    def get_children(self, obj):
        if obj.children.exists():
            return CategorySerializer(obj.children.all(), many=True).data
        return []


class ProductListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    videos = ProductVideoSerializer(many=True, read_only=True)
    metal_type_display = serializers.CharField(source='get_metal_type_display', read_only=True)
    karat_display = serializers.CharField(source='get_karat_display', read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'category', 'description',
            'metal_type', 'metal_type_display', 'karat', 'karat_display',
            'weight', 'price', 'stock_code', 'image', 'images', 'videos', 'is_featured', 'is_best_seller', 'is_recommended', 'created_at'
        ]


class ProductDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    videos = ProductVideoSerializer(many=True, read_only=True)
    metal_type_display = serializers.CharField(source='get_metal_type_display', read_only=True)
    karat_display = serializers.CharField(source='get_karat_display', read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'category', 'description',
            'metal_type', 'metal_type_display', 'karat', 'karat_display',
            'weight', 'price', 'stock_code', 'image', 'images', 'videos',
            'is_available', 'is_featured', 'is_best_seller', 'is_recommended', 'created_at', 'updated_at'
        ]
