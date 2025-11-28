from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kategori Adı")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="URL")
    description = models.TextField(blank=True, verbose_name="Açıklama")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Güncellenme Tarihi")

    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategoriler"
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    KARAT_CHOICES = [
        ('8', '8 Ayar'),
        ('14', '14 Ayar'),
        ('18', '18 Ayar'),
        ('22', '22 Ayar'),
        ('24', '24 Ayar'),
    ]

    METAL_TYPE_CHOICES = [
        ('gold', 'Altın'),
        ('silver', 'Gümüş'),
        ('platinum', 'Platin'),
        ('rose_gold', 'Rose Altın'),
        ('white_gold', 'Beyaz Altın'),
    ]

    name = models.CharField(max_length=200, verbose_name="Ürün Adı")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="Kategori")
    description = models.TextField(verbose_name="Açıklama")

    metal_type = models.CharField(max_length=20, choices=METAL_TYPE_CHOICES, verbose_name="Metal Tipi")
    karat = models.CharField(max_length=2, choices=KARAT_CHOICES, blank=True, verbose_name="Ayar")
    weight = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))], verbose_name="Ağırlık (gram)")

    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))], verbose_name="Fiyat (TL)")
    stock = models.PositiveIntegerField(default=0, verbose_name="Stok")

    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name="Ürün Resmi")

    is_available = models.BooleanField(default=True, verbose_name="Satışta")
    is_featured = models.BooleanField(default=False, verbose_name="Öne Çıkan")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Güncellenme Tarihi")

    class Meta:
        verbose_name = "Ürün"
        verbose_name_plural = "Ürünler"
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name="Ürün")
    image = models.ImageField(upload_to='products/%Y/%m/%d/', verbose_name="Resim")
    alt_text = models.CharField(max_length=200, blank=True, verbose_name="Alternatif Metin")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")

    class Meta:
        verbose_name = "Ürün Resmi"
        verbose_name_plural = "Ürün Resimleri"
        ordering = ['created_at']

    def __str__(self):
        return f"{self.product.name} - Resim"
