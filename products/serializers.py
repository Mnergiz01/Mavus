from rest_framework import serializers
from .models import Category, Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'image_file', 'image_url', 'alt_text', 'is_video', 'order']

    def get_image_url(self, obj):
        return obj.get_image_url()


class CategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description', 'parent', 'image', 'image_file', 'image_url', 'children']

    def get_image_url(self, obj):
        return obj.get_image_url()

    def get_children(self, obj):
        # Prevent infinite recursion by limiting depth
        depth = self.context.get('depth', 0)
        if depth > 2:  # Maximum 2 levels of nesting
            return []

        if obj.children.exists():
            # Pass increased depth to child serializers
            context = self.context.copy()
            context['depth'] = depth + 1
            return CategorySerializer(obj.children.all(), many=True, context=context).data
        return []


class ProductListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    metal_type_display = serializers.CharField(source='get_metal_type_display', read_only=True)
    karat_display = serializers.CharField(source='get_karat_display', read_only=True)
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'category', 'description',
            'metal_type', 'metal_type_display', 'karat', 'karat_display',
            'weight', 'price', 'stock_code', 'image', 'image_file', 'image_url', 'images', 'is_featured', 'is_best_seller', 'is_recommended', 'created_at'
        ]

    def get_image_url(self, obj):
        return obj.get_image_url()


class ProductDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    metal_type_display = serializers.CharField(source='get_metal_type_display', read_only=True)
    karat_display = serializers.CharField(source='get_karat_display', read_only=True)
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'category', 'description',
            'metal_type', 'metal_type_display', 'karat', 'karat_display',
            'weight', 'price', 'stock_code', 'image', 'image_file', 'image_url', 'images',
            'is_available', 'is_featured', 'is_best_seller', 'is_recommended', 'created_at', 'updated_at'
        ]

    def get_image_url(self, obj):
        return obj.get_image_url()
