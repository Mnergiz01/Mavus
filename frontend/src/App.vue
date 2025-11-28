<script setup>
import { ref, onMounted, computed } from 'vue'
import axios from 'axios'
import {
  MagnifyingGlassIcon,
  ShoppingBagIcon,
  Bars3Icon,
  XMarkIcon,
  SparklesIcon,
  StarIcon,
  ShieldCheckIcon,
  TruckIcon,
  PhoneIcon,
  EnvelopeIcon,
  MapPinIcon
} from '@heroicons/vue/24/outline'

const API_URL = 'http://127.0.0.1:8000/api'

const products = ref([])
const categories = ref([])
const selectedCategory = ref(null)
const searchQuery = ref('')
const isLoading = ref(false)
const selectedProduct = ref(null)
const showMobileMenu = ref(false)
const scrolled = ref(false)
const sortBy = ref('newest')

const filteredProducts = computed(() => {
  let filtered = products.value

  if (selectedCategory.value) {
    filtered = filtered.filter(p => p.category.slug === selectedCategory.value)
  }

  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    filtered = filtered.filter(p =>
      p.name.toLowerCase().includes(query) ||
      p.description.toLowerCase().includes(query)
    )
  }

  // Sorting
  if (sortBy.value === 'price-low') {
    filtered = [...filtered].sort((a, b) => parseFloat(a.price) - parseFloat(b.price))
  } else if (sortBy.value === 'price-high') {
    filtered = [...filtered].sort((a, b) => parseFloat(b.price) - parseFloat(a.price))
  } else if (sortBy.value === 'name') {
    filtered = [...filtered].sort((a, b) => a.name.localeCompare(b.name))
  }

  return filtered
})

const featuredProducts = computed(() => {
  return products.value.filter(p => p.is_featured)
})

async function fetchData() {
  isLoading.value = true
  try {
    const [productsRes, categoriesRes] = await Promise.all([
      axios.get(`${API_URL}/products/`),
      axios.get(`${API_URL}/categories/`)
    ])
    products.value = productsRes.data.results || productsRes.data
    categories.value = categoriesRes.data.results || categoriesRes.data
  } catch (error) {
    console.error('Veri yüklenirken hata:', error)
  } finally {
    isLoading.value = false
  }
}

function selectCategory(slug) {
  selectedCategory.value = selectedCategory.value === slug ? null : slug
  showMobileMenu.value = false
  window.scrollTo({ top: 600, behavior: 'smooth' })
}

function viewProduct(product) {
  selectedProduct.value = product
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

function closeProductDetail() {
  selectedProduct.value = null
}

function handleScroll() {
  scrolled.value = window.scrollY > 50
}

onMounted(() => {
  fetchData()
  window.addEventListener('scroll', handleScroll)
})
</script>

<template>
  <div class="min-h-screen bg-gradient-to-br from-slate-50 via-amber-50/30 to-slate-50">
    <!-- Premium Header -->
    <header
      :class="[
        'fixed top-0 left-0 right-0 z-50 transition-all duration-500',
        scrolled ? 'bg-white/95 backdrop-blur-lg shadow-xl py-3' : 'bg-gradient-to-b from-slate-900/95 to-slate-800/90 backdrop-blur-md py-5'
      ]"
    >
      <div class="container mx-auto px-4">
        <div class="flex items-center justify-between">
          <!-- Logo -->
          <div class="flex items-center space-x-3 group cursor-pointer" @click="selectedProduct = null; selectedCategory = null">
            <div class="relative">
              <SparklesIcon
                :class="[
                  'h-10 w-10 transition-all duration-300',
                  scrolled ? 'text-amber-600' : 'text-amber-400'
                ]"
              />
              <div class="absolute inset-0 bg-amber-400 blur-xl opacity-20 group-hover:opacity-40 transition-opacity"></div>
            </div>
            <div>
              <h1
                :class="[
                  'text-3xl font-serif font-bold tracking-widest transition-colors duration-300',
                  scrolled ? 'text-slate-900' : 'text-white'
                ]"
              >
                MAVUS
              </h1>
              <p :class="['text-xs tracking-widest uppercase', scrolled ? 'text-amber-600' : 'text-amber-400']">
                Haute Joaillerie
              </p>
            </div>
          </div>

          <!-- Mobile menu button -->
          <button
            @click="showMobileMenu = !showMobileMenu"
            :class="[
              'md:hidden p-2 rounded-lg transition-colors',
              scrolled ? 'text-slate-900 hover:bg-slate-100' : 'text-white hover:bg-white/10'
            ]"
          >
            <Bars3Icon v-if="!showMobileMenu" class="h-7 w-7" />
            <XMarkIcon v-else class="h-7 w-7" />
          </button>

          <!-- Desktop Navigation -->
          <nav class="hidden md:flex items-center space-x-8">
            <button
              @click="selectCategory(null)"
              :class="[
                'font-medium transition-all duration-300 relative group',
                selectedCategory === null
                  ? (scrolled ? 'text-amber-600' : 'text-amber-400')
                  : (scrolled ? 'text-slate-700 hover:text-amber-600' : 'text-white/80 hover:text-white')
              ]"
            >
              Koleksiyon
              <span class="absolute -bottom-1 left-0 w-0 h-0.5 bg-amber-500 group-hover:w-full transition-all duration-300"></span>
            </button>
            <button
              v-for="cat in categories"
              :key="cat.id"
              @click="selectCategory(cat.slug)"
              :class="[
                'font-medium transition-all duration-300 relative group',
                selectedCategory === cat.slug
                  ? (scrolled ? 'text-amber-600' : 'text-amber-400')
                  : (scrolled ? 'text-slate-700 hover:text-amber-600' : 'text-white/80 hover:text-white')
              ]"
            >
              {{ cat.name }}
              <span class="absolute -bottom-1 left-0 w-0 h-0.5 bg-amber-500 group-hover:w-full transition-all duration-300"></span>
            </button>
            <a
              href="http://127.0.0.1:8000/admin/"
              target="_blank"
              class="px-5 py-2 bg-gradient-to-r from-amber-600 to-amber-500 text-white rounded-full hover:from-amber-500 hover:to-amber-600 transition-all duration-300 shadow-lg hover:shadow-amber-500/50 font-medium"
            >
              Admin
            </a>
          </nav>
        </div>

        <!-- Mobile Navigation -->
        <nav
          v-if="showMobileMenu"
          class="md:hidden mt-6 pb-4 space-y-3 border-t border-white/10 pt-4"
        >
          <button
            @click="selectCategory(null)"
            :class="[
              'block w-full text-left px-4 py-3 rounded-lg font-medium transition-all duration-300',
              selectedCategory === null
                ? 'bg-amber-500 text-white'
                : (scrolled ? 'text-slate-700 hover:bg-slate-100' : 'text-white hover:bg-white/10')
            ]"
          >
            Tüm Koleksiyon
          </button>
          <button
            v-for="cat in categories"
            :key="cat.id"
            @click="selectCategory(cat.slug)"
            :class="[
              'block w-full text-left px-4 py-3 rounded-lg font-medium transition-all duration-300',
              selectedCategory === cat.slug
                ? 'bg-amber-500 text-white'
                : (scrolled ? 'text-slate-700 hover:bg-slate-100' : 'text-white hover:bg-white/10')
            ]"
          >
            {{ cat.name }}
          </button>
        </nav>
      </div>
    </header>

    <!-- Hero Section -->
    <section
      v-if="!selectedProduct && featuredProducts.length > 0"
      class="relative pt-32 pb-20 overflow-hidden bg-gradient-to-br from-slate-900 via-slate-800 to-amber-900"
    >
      <!-- Animated Background -->
      <div class="absolute inset-0 opacity-10">
        <div class="absolute top-20 left-20 w-72 h-72 bg-amber-500 rounded-full blur-3xl animate-pulse"></div>
        <div class="absolute bottom-20 right-20 w-96 h-96 bg-amber-400 rounded-full blur-3xl animate-pulse delay-1000"></div>
      </div>

      <div class="container mx-auto px-4 relative z-10">
        <div class="text-center mb-16 animate-fade-in">
          <p class="text-amber-400 text-sm tracking-widest uppercase mb-4 font-semibold">Lüks & Zarafet</p>
          <h2 class="text-6xl md:text-7xl font-serif font-bold text-white mb-6 tracking-tight">
            Özel Koleksiyon
          </h2>
          <p class="text-xl text-slate-300 max-w-2xl mx-auto leading-relaxed">
            Her parça, ustalıkla işlenmiş ve benzersiz tasarımlarla hayat bulmuş bir sanat eseridir
          </p>
        </div>

        <!-- Featured Products Carousel -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-7xl mx-auto">
          <div
            v-for="(product, index) in featuredProducts"
            :key="product.id"
            @click="viewProduct(product)"
            class="group cursor-pointer"
            :style="{ animationDelay: `${index * 150}ms` }"
          >
            <div class="relative bg-white rounded-2xl overflow-hidden shadow-2xl hover:shadow-amber-500/30 transition-all duration-500 transform hover:-translate-y-4">
              <!-- Featured Badge -->
              <div class="absolute top-4 left-4 z-20 bg-gradient-to-r from-amber-500 to-amber-600 text-white px-4 py-2 rounded-full text-xs font-bold tracking-wider shadow-lg flex items-center space-x-1">
                <StarIcon class="h-4 w-4" />
                <span>ÖZEL</span>
              </div>

              <!-- Product Image -->
              <div class="aspect-square bg-gradient-to-br from-amber-50 to-slate-100 overflow-hidden relative">
                <img
                  v-if="product.image"
                  :src="product.image"
                  :alt="product.name"
                  class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700"
                />
                <div v-else class="absolute inset-0 flex items-center justify-center text-9xl">💎</div>

                <!-- Overlay -->
                <div class="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>

                <!-- Quick View Button -->
                <div class="absolute bottom-4 left-1/2 transform -translate-x-1/2 translate-y-8 group-hover:translate-y-0 opacity-0 group-hover:opacity-100 transition-all duration-500">
                  <button class="px-6 py-3 bg-white text-slate-900 rounded-full font-semibold shadow-xl hover:bg-amber-500 hover:text-white transition-colors duration-300">
                    Detayları Gör
                  </button>
                </div>
              </div>

              <!-- Product Info -->
              <div class="p-6">
                <p class="text-amber-600 text-sm font-semibold mb-2 tracking-wide">{{ product.category.name }}</p>
                <h3 class="text-2xl font-serif font-bold text-slate-900 mb-3 line-clamp-2 group-hover:text-amber-600 transition-colors">
                  {{ product.name }}
                </h3>

                <div class="flex items-center justify-between mb-4">
                  <div class="text-sm text-slate-600 space-y-1">
                    <p class="flex items-center space-x-2">
                      <span class="font-medium">{{ product.metal_type_display }}</span>
                      <span v-if="product.karat" class="text-amber-600">• {{ product.karat_display }}</span>
                    </p>
                    <p class="text-xs">{{ product.weight }} gram</p>
                  </div>
                </div>

                <div class="flex items-center justify-between pt-4 border-t border-slate-200">
                  <div class="text-3xl font-bold text-slate-900">
                    <span class="text-xl text-slate-600">₺</span>{{ parseFloat(product.price).toLocaleString('tr-TR') }}
                  </div>
                  <ShoppingBagIcon class="h-6 w-6 text-amber-600 group-hover:scale-110 transition-transform" />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Product Detail View -->
    <div v-if="selectedProduct" class="pt-32 pb-20 bg-white">
      <div class="container mx-auto px-4">
        <button
          @click="closeProductDetail"
          class="mb-8 flex items-center space-x-2 text-slate-600 hover:text-amber-600 font-semibold transition-colors group"
        >
          <svg class="h-5 w-5 group-hover:-translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/>
          </svg>
          <span>Koleksiyona Dön</span>
        </button>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 max-w-7xl mx-auto">
          <!-- Product Images -->
          <div class="space-y-4">
            <div class="aspect-square bg-gradient-to-br from-amber-50 to-slate-100 rounded-3xl overflow-hidden shadow-2xl relative group">
              <img
                v-if="selectedProduct.image"
                :src="selectedProduct.image"
                :alt="selectedProduct.name"
                class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700"
              />
              <div v-else class="absolute inset-0 flex items-center justify-center text-9xl">💎</div>

              <div v-if="selectedProduct.is_featured" class="absolute top-6 right-6 bg-gradient-to-r from-amber-500 to-amber-600 text-white px-5 py-2 rounded-full text-sm font-bold tracking-wider shadow-xl flex items-center space-x-2">
                <StarIcon class="h-5 w-5" />
                <span>ÖZEL PARÇA</span>
              </div>
            </div>

            <!-- Additional Images Gallery -->
            <div v-if="selectedProduct.images && selectedProduct.images.length > 0" class="grid grid-cols-4 gap-4">
              <div
                v-for="image in selectedProduct.images"
                :key="image.id"
                class="aspect-square bg-gradient-to-br from-amber-50 to-slate-100 rounded-xl overflow-hidden cursor-pointer hover:ring-4 hover:ring-amber-500 transition-all duration-300"
              >
                <img :src="image.image" :alt="image.alt_text" class="w-full h-full object-cover" />
              </div>
            </div>
          </div>

          <!-- Product Details -->
          <div class="flex flex-col">
            <div class="mb-6">
              <p class="text-amber-600 text-sm font-bold tracking-widest uppercase mb-3">{{ selectedProduct.category.name }}</p>
              <h1 class="text-5xl font-serif font-bold text-slate-900 mb-6 leading-tight">
                {{ selectedProduct.name }}
              </h1>
              <p class="text-lg text-slate-600 leading-relaxed">
                {{ selectedProduct.description }}
              </p>
            </div>

            <!-- Specifications -->
            <div class="bg-gradient-to-br from-slate-50 to-amber-50/30 rounded-2xl p-8 mb-8 space-y-4">
              <h3 class="text-xl font-serif font-bold text-slate-900 mb-6">Ürün Özellikleri</h3>

              <div class="grid grid-cols-2 gap-6">
                <div class="space-y-2">
                  <p class="text-sm text-slate-500 uppercase tracking-wider">Metal</p>
                  <p class="text-lg font-semibold text-slate-900">{{ selectedProduct.metal_type_display }}</p>
                </div>

                <div v-if="selectedProduct.karat" class="space-y-2">
                  <p class="text-sm text-slate-500 uppercase tracking-wider">Ayar</p>
                  <p class="text-lg font-semibold text-slate-900">{{ selectedProduct.karat_display }}</p>
                </div>

                <div class="space-y-2">
                  <p class="text-sm text-slate-500 uppercase tracking-wider">Ağırlık</p>
                  <p class="text-lg font-semibold text-slate-900">{{ selectedProduct.weight }} gram</p>
                </div>

                <div class="space-y-2">
                  <p class="text-sm text-slate-500 uppercase tracking-wider">Stok</p>
                  <p class="text-lg font-semibold" :class="selectedProduct.stock > 5 ? 'text-green-600' : 'text-amber-600'">
                    {{ selectedProduct.stock }} adet
                  </p>
                </div>
              </div>
            </div>

            <!-- Price and CTA -->
            <div class="mt-auto space-y-6">
              <div class="bg-gradient-to-r from-slate-900 to-slate-800 rounded-2xl p-8 text-center">
                <p class="text-slate-400 text-sm mb-2 tracking-widest uppercase">Fiyat</p>
                <div class="text-5xl font-bold text-white mb-1">
                  ₺{{ parseFloat(selectedProduct.price).toLocaleString('tr-TR') }}
                </div>
                <p class="text-slate-400 text-sm">KDV Dahil</p>
              </div>

              <div class="grid grid-cols-2 gap-4">
                <button class="px-8 py-4 bg-gradient-to-r from-amber-600 to-amber-500 text-white rounded-xl font-bold text-lg hover:from-amber-500 hover:to-amber-600 transition-all duration-300 shadow-lg hover:shadow-amber-500/50 transform hover:-translate-y-1 flex items-center justify-center space-x-2">
                  <ShoppingBagIcon class="h-6 w-6" />
                  <span>İletişime Geç</span>
                </button>
                <button class="px-8 py-4 bg-white border-2 border-slate-300 text-slate-900 rounded-xl font-bold text-lg hover:border-amber-500 hover:text-amber-600 transition-all duration-300 flex items-center justify-center space-x-2">
                  <PhoneIcon class="h-6 w-6" />
                  <span>Ara</span>
                </button>
              </div>
            </div>

            <!-- Trust Badges -->
            <div class="grid grid-cols-3 gap-4 mt-8 pt-8 border-t border-slate-200">
              <div class="text-center space-y-2">
                <ShieldCheckIcon class="h-8 w-8 mx-auto text-amber-600" />
                <p class="text-xs font-medium text-slate-600">Garanti</p>
              </div>
              <div class="text-center space-y-2">
                <TruckIcon class="h-8 w-8 mx-auto text-amber-600" />
                <p class="text-xs font-medium text-slate-600">Hızlı Teslimat</p>
              </div>
              <div class="text-center space-y-2">
                <StarIcon class="h-8 w-8 mx-auto text-amber-600" />
                <p class="text-xs font-medium text-slate-600">Premium Kalite</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Search and Filter Section -->
    <section v-if="!selectedProduct" class="py-16 bg-white border-y border-slate-200">
      <div class="container mx-auto px-4">
        <div class="max-w-4xl mx-auto">
          <div class="flex flex-col md:flex-row gap-4">
            <!-- Search -->
            <div class="flex-1 relative">
              <MagnifyingGlassIcon class="absolute left-4 top-1/2 transform -translate-y-1/2 h-6 w-6 text-slate-400" />
              <input
                v-model="searchQuery"
                type="text"
                placeholder="Ürün ara..."
                class="w-full pl-12 pr-4 py-4 border-2 border-slate-200 rounded-xl focus:border-amber-500 focus:outline-none text-lg transition-colors"
              />
            </div>

            <!-- Sort -->
            <select
              v-model="sortBy"
              class="px-6 py-4 border-2 border-slate-200 rounded-xl focus:border-amber-500 focus:outline-none text-slate-700 font-medium cursor-pointer transition-colors"
            >
              <option value="newest">En Yeni</option>
              <option value="price-low">Fiyat (Düşük)</option>
              <option value="price-high">Fiyat (Yüksek)</option>
              <option value="name">İsim (A-Z)</option>
            </select>
          </div>
        </div>
      </div>
    </section>

    <!-- Products Grid -->
    <section v-if="!selectedProduct" class="py-20 bg-gradient-to-b from-white to-slate-50">
      <div class="container mx-auto px-4">
        <div class="text-center mb-16">
          <h2 class="text-5xl font-serif font-bold text-slate-900 mb-4">
            {{ selectedCategory ? categories.find(c => c.slug === selectedCategory)?.name : 'Tüm Koleksiyon' }}
          </h2>
          <p class="text-lg text-slate-600">{{ filteredProducts.length }} ürün bulundu</p>
        </div>

        <!-- Loading -->
        <div v-if="isLoading" class="text-center py-20">
          <div class="inline-block animate-spin rounded-full h-16 w-16 border-4 border-amber-500 border-t-transparent mb-4"></div>
          <p class="text-slate-600 text-lg">Yükleniyor...</p>
        </div>

        <!-- No Products -->
        <div v-else-if="filteredProducts.length === 0" class="text-center py-20">
          <div class="text-8xl mb-6">🔍</div>
          <h3 class="text-3xl font-serif font-bold text-slate-900 mb-4">Ürün Bulunamadı</h3>
          <p class="text-lg text-slate-600 mb-8">Arama kriterlerinize uygun ürün bulunmamaktadır.</p>
          <button
            @click="searchQuery = ''; selectedCategory = null"
            class="px-8 py-4 bg-gradient-to-r from-amber-600 to-amber-500 text-white rounded-xl font-semibold hover:from-amber-500 hover:to-amber-600 transition-all duration-300 shadow-lg"
          >
            Tüm Ürünleri Göster
          </button>
        </div>

        <!-- Products Grid -->
        <div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">
          <div
            v-for="product in filteredProducts"
            :key="product.id"
            @click="viewProduct(product)"
            class="group cursor-pointer"
          >
            <div class="bg-white rounded-2xl overflow-hidden shadow-lg hover:shadow-2xl transition-all duration-500 transform hover:-translate-y-2">
              <!-- Product Image -->
              <div class="aspect-square bg-gradient-to-br from-amber-50 to-slate-100 overflow-hidden relative">
                <img
                  v-if="product.image"
                  :src="product.image"
                  :alt="product.name"
                  class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700"
                />
                <div v-else class="absolute inset-0 flex items-center justify-center text-7xl">💎</div>

                <!-- Badges -->
                <div class="absolute top-3 left-3 space-y-2">
                  <span v-if="product.is_featured" class="block bg-gradient-to-r from-amber-500 to-amber-600 text-white px-3 py-1 rounded-full text-xs font-bold shadow-lg">
                    ÖZEL
                  </span>
                  <span v-if="product.stock < 3" class="block bg-red-500 text-white px-3 py-1 rounded-full text-xs font-bold shadow-lg">
                    SON {{ product.stock }} ADET
                  </span>
                </div>

                <!-- Quick Actions -->
                <div class="absolute bottom-3 right-3 opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                  <button class="p-3 bg-white rounded-full shadow-xl hover:bg-amber-500 hover:text-white transition-colors">
                    <MagnifyingGlassIcon class="h-5 w-5" />
                  </button>
                </div>
              </div>

              <!-- Product Info -->
              <div class="p-5">
                <div class="flex items-center justify-between mb-2">
                  <span class="text-sm text-amber-600 font-semibold">{{ product.category.name }}</span>
                  <span v-if="product.is_featured" class="text-amber-500">
                    <StarIcon class="h-4 w-4 fill-current" />
                  </span>
                </div>

                <h3 class="text-xl font-serif font-bold text-slate-900 mb-3 line-clamp-2 group-hover:text-amber-600 transition-colors">
                  {{ product.name }}
                </h3>

                <div class="flex items-center justify-between text-sm text-slate-600 mb-4">
                  <span class="font-medium">{{ product.metal_type_display }}</span>
                  <span v-if="product.karat" class="text-xs bg-slate-100 px-2 py-1 rounded">{{ product.karat_display }}</span>
                </div>

                <div class="flex items-end justify-between pt-4 border-t border-slate-200">
                  <div>
                    <p class="text-xs text-slate-500 mb-1">{{ product.weight }}g</p>
                    <div class="text-2xl font-bold text-slate-900">
                      ₺{{ parseFloat(product.price).toLocaleString('tr-TR') }}
                    </div>
                  </div>
                  <ShoppingBagIcon class="h-6 w-6 text-amber-600 group-hover:scale-110 transition-transform" />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer class="bg-gradient-to-b from-slate-900 to-slate-950 text-white py-16">
      <div class="container mx-auto px-4">
        <div class="grid grid-cols-1 md:grid-cols-4 gap-12 mb-12">
          <!-- Brand -->
          <div class="md:col-span-2">
            <div class="flex items-center space-x-3 mb-6">
              <SparklesIcon class="h-10 w-10 text-amber-400" />
              <div>
                <h3 class="text-3xl font-serif font-bold">MAVUS</h3>
                <p class="text-xs text-amber-400 tracking-widest uppercase">Haute Joaillerie</p>
              </div>
            </div>
            <p class="text-slate-400 leading-relaxed mb-6 max-w-md">
              Zarafet ve lüksün buluştuğu noktada, her parça özenle tasarlanmış ve benzersiz bir sanat eserine dönüştürülmüştür.
            </p>
            <div class="flex space-x-4">
              <a href="#" class="w-10 h-10 bg-slate-800 rounded-full flex items-center justify-center hover:bg-amber-600 transition-colors">
                <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
              </a>
              <a href="#" class="w-10 h-10 bg-slate-800 rounded-full flex items-center justify-center hover:bg-amber-600 transition-colors">
                <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
              </a>
              <a href="#" class="w-10 h-10 bg-slate-800 rounded-full flex items-center justify-center hover:bg-amber-600 transition-colors">
                <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24"><path d="M23.953 4.57a10 10 0 01-2.825.775 4.958 4.958 0 002.163-2.723c-.951.555-2.005.959-3.127 1.184a4.92 4.92 0 00-8.384 4.482C7.69 8.095 4.067 6.13 1.64 3.162a4.822 4.822 0 00-.666 2.475c0 1.71.87 3.213 2.188 4.096a4.904 4.904 0 01-2.228-.616v.06a4.923 4.923 0 003.946 4.827 4.996 4.996 0 01-2.212.085 4.936 4.936 0 004.604 3.417 9.867 9.867 0 01-6.102 2.105c-.39 0-.779-.023-1.17-.067a13.995 13.995 0 007.557 2.209c9.053 0 13.998-7.496 13.998-13.985 0-.21 0-.42-.015-.63A9.935 9.935 0 0024 4.59z"/></svg>
              </a>
            </div>
          </div>

          <!-- Quick Links -->
          <div>
            <h4 class="text-lg font-bold mb-6">Hızlı Bağlantılar</h4>
            <ul class="space-y-3">
              <li><a href="#" class="text-slate-400 hover:text-amber-400 transition-colors">Hakkımızda</a></li>
              <li><a href="#" class="text-slate-400 hover:text-amber-400 transition-colors">Koleksiyonlar</a></li>
              <li><a href="#" class="text-slate-400 hover:text-amber-400 transition-colors">Mağazalarımız</a></li>
              <li><a href="#" class="text-slate-400 hover:text-amber-400 transition-colors">İletişim</a></li>
            </ul>
          </div>

          <!-- Contact -->
          <div>
            <h4 class="text-lg font-bold mb-6">İletişim</h4>
            <ul class="space-y-4">
              <li class="flex items-start space-x-3">
                <PhoneIcon class="h-5 w-5 text-amber-400 mt-1 flex-shrink-0" />
                <span class="text-slate-400">+90 (212) 555 00 00</span>
              </li>
              <li class="flex items-start space-x-3">
                <EnvelopeIcon class="h-5 w-5 text-amber-400 mt-1 flex-shrink-0" />
                <span class="text-slate-400">info@mavus.com</span>
              </li>
              <li class="flex items-start space-x-3">
                <MapPinIcon class="h-5 w-5 text-amber-400 mt-1 flex-shrink-0" />
                <span class="text-slate-400">İstanbul, Türkiye</span>
              </li>
            </ul>
          </div>
        </div>

        <div class="border-t border-slate-800 pt-8 text-center">
          <p class="text-slate-400 text-sm">
            &copy; 2025 MAVUS Kuyumculuk. Tüm hakları saklıdır.
          </p>
        </div>
      </div>
    </footer>
  </div>
</template>

<style scoped>
@keyframes fade-in {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fade-in {
  animation: fade-in 1s ease-out;
}

.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
