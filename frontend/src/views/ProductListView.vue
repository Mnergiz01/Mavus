<template>
  <div class="pt-32 pb-20 bg-gradient-to-b from-white to-slate-50">
    <div class="container mx-auto px-4">
      <!-- Back Button -->
      <button
        @click="$router.push('/')"
        class="mb-8 flex items-center space-x-2 text-slate-600 hover:text-amber-600 font-semibold transition-colors group animate-slide-in-left"
      >
        <svg class="h-5 w-5 group-hover:-translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/>
        </svg>
        <span>Ana Sayfaya Dön</span>
      </button>

      <div class="text-center mb-8 animate-fade-in">
        <h2 class="text-4xl font-serif font-bold text-slate-900 mb-3">
          {{ title }}
        </h2>
        <p class="text-base text-slate-600">{{ filteredProducts.length }} ürün bulundu</p>
      </div>

      <!-- Filter Toggle Button -->
      <div v-if="$route.params.slug" class="mb-6 flex justify-center animate-fade-in">
        <button
          @click="showFilters = !showFilters"
          class="px-6 py-3 bg-white hover:bg-amber-50 border-2 border-amber-500 text-amber-600 rounded-xl font-bold transition-all duration-300 flex items-center space-x-2 shadow-md hover:shadow-lg"
        >
          <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z"/>
          </svg>
          <span>{{ showFilters ? 'Filtreleri Gizle' : 'Filtrele' }}</span>
          <svg
            class="h-4 w-4 transition-transform duration-300"
            :class="{ 'rotate-180': showFilters }"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
          </svg>
        </button>
      </div>

      <!-- Filters Section -->
      <transition
        enter-active-class="transition-all duration-300 ease-out"
        enter-from-class="opacity-0 -translate-y-4"
        enter-to-class="opacity-100 translate-y-0"
        leave-active-class="transition-all duration-200 ease-in"
        leave-from-class="opacity-100 translate-y-0"
        leave-to-class="opacity-0 -translate-y-4"
      >
        <div v-if="$route.params.slug && showFilters" class="mb-8 bg-white rounded-2xl shadow-lg p-6">
          <div class="grid grid-cols-1 md:grid-cols-4 gap-6">
            <!-- Metal Type Filter -->
            <div>
              <label class="block text-sm font-bold text-slate-700 mb-2">Metal Tipi</label>
              <select
                v-model="selectedMetalType"
                class="w-full px-4 py-2.5 bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-amber-500 focus:border-amber-500 transition-all"
              >
                <option :value="null">Tümü</option>
                <option value="gold">Altın</option>
                <option value="silver">Gümüş</option>
                <option value="platinum">Platin</option>
                <option value="rose_gold">Rose Altın</option>
                <option value="white_gold">Beyaz Altın</option>
              </select>
            </div>

            <!-- Karat Filter -->
            <div>
              <label class="block text-sm font-bold text-slate-700 mb-2">Ayar</label>
              <select
                v-model="selectedKarat"
                class="w-full px-4 py-2.5 bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-amber-500 focus:border-amber-500 transition-all"
              >
                <option :value="null">Tümü</option>
                <option v-for="karat in karats" :key="karat" :value="karat">{{ karat }} Ayar</option>
              </select>
            </div>

            <!-- Sort By -->
            <div>
              <label class="block text-sm font-bold text-slate-700 mb-2">Sırala</label>
              <select
                v-model="sortBy"
                class="w-full px-4 py-2.5 bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-amber-500 focus:border-amber-500 transition-all"
              >
                <option value="newest">En Yeni</option>
                <option value="price-low">Fiyat (Düşükten Yükseğe)</option>
                <option value="price-high">Fiyat (Yüksekten Düşüğe)</option>
                <option value="name">İsme Göre</option>
              </select>
            </div>

            <!-- Clear Filters Button -->
            <div class="flex items-end">
              <button
                @click="clearFilters"
                class="w-full px-4 py-2.5 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-xl font-semibold transition-all duration-300 flex items-center justify-center space-x-2"
              >
                <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
                </svg>
                <span>Filtreleri Temizle</span>
              </button>
            </div>
          </div>
        </div>
      </transition>

      <!-- Loading -->
      <div v-if="isLoading" class="text-center py-20">
        <div class="inline-block animate-spin rounded-full h-16 w-16 border-4 border-amber-500 border-t-transparent mb-4"></div>
        <p class="text-slate-600 text-lg">Yükleniyor...</p>
      </div>

      <!-- No Products -->
      <div v-else-if="filteredProducts.length === 0" class="text-center py-20">
        <div class="text-8xl mb-6">🔍</div>
        <h3 class="text-3xl font-serif font-bold text-slate-900 mb-4">Ürün Bulunamadı</h3>
        <p class="text-lg text-slate-600 mb-8">
          Bu kategoride ürün bulunmamaktadır.
        </p>
        <button
          @click="$router.push('/')"
          class="px-8 py-4 bg-gradient-to-r from-amber-600 to-amber-500 text-white rounded-xl font-semibold hover:from-amber-500 hover:to-amber-600 transition-all duration-300 shadow-lg"
        >
          Ana Sayfaya Dön
        </button>
      </div>

      <!-- Products Grid -->
      <div v-else class="grid grid-cols-2 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-3 sm:gap-6">
        <div
          v-for="(product, index) in filteredProducts"
          :key="product.id"
          @click="$router.push(`/products/${product.slug}`)"
          class="group cursor-pointer animate-scale-in bg-white rounded-2xl overflow-hidden shadow-lg hover:shadow-2xl transition-all duration-500 transform hover:-translate-y-3 border border-slate-100 hover:border-amber-200"
          :style="{ animationDelay: `${(index % 8) * 0.05}s` }"
        >
          <!-- Product Image -->
          <div class="aspect-square bg-gradient-to-br from-amber-50 via-white to-slate-50 overflow-hidden relative">
            <img
              v-if="product.image"
              :src="product.image"
              :alt="product.name"
              class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700"
            />
            <div v-else class="absolute inset-0 flex items-center justify-center text-7xl">💎</div>

            <!-- Gradient Overlay -->
            <div class="absolute inset-0 bg-gradient-to-t from-black/20 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>

            <!-- Badges -->
            <div class="absolute top-3 left-3 flex flex-col gap-2 z-10">
              <span v-if="product.is_featured" class="flex items-center gap-1.5 bg-gradient-to-r from-amber-500 to-amber-600 text-white px-3 py-1.5 rounded-full text-xs font-bold shadow-xl backdrop-blur-sm">
                <StarIcon class="h-3.5 w-3.5 fill-current" />
                ÖZEL
              </span>
              <span v-if="product.stock < 3" class="flex items-center gap-1.5 bg-gradient-to-r from-red-500 to-red-600 text-white px-3 py-1.5 rounded-full text-xs font-bold shadow-xl backdrop-blur-sm animate-pulse">
                <span class="w-1.5 h-1.5 rounded-full bg-white"></span>
                SON {{ product.stock }} ADET
              </span>
            </div>

            <!-- View Details Button -->
            <div class="absolute bottom-4 left-1/2 -translate-x-1/2 opacity-0 group-hover:opacity-100 transition-all duration-500 transform translate-y-4 group-hover:translate-y-0">
              <button class="px-6 py-2.5 bg-white/95 backdrop-blur-sm text-slate-900 rounded-xl font-bold text-sm shadow-xl hover:bg-amber-500 hover:text-white transition-all duration-300 hover:scale-105">
                Detayları Gör
              </button>
            </div>
          </div>

          <!-- Product Info -->
          <div class="p-3 sm:p-5">
            <div class="flex items-center justify-between mb-2">
              <span class="text-[10px] sm:text-xs text-amber-600 font-bold tracking-wider uppercase">{{ product.category?.name || 'Ürün' }}</span>
              <span v-if="product.is_featured" class="text-amber-500">
                <StarIcon class="h-3 w-3 sm:h-4 sm:w-4 fill-current drop-shadow-sm" />
              </span>
            </div>

            <h3 class="text-sm sm:text-lg font-serif font-bold text-slate-900 mb-2 sm:mb-3 line-clamp-2 group-hover:text-amber-600 transition-colors leading-tight">
              {{ product.name }}
            </h3>

            <!-- Specs -->
            <div class="flex items-center gap-1 sm:gap-2 mb-3 sm:mb-4">
              <div class="flex-1">
                <p class="text-[9px] sm:text-xs text-slate-500 mb-0.5">Metal</p>
                <p class="text-xs sm:text-sm font-semibold text-slate-700">{{ product.metal_type_display }}</p>
              </div>
              <div v-if="product.karat" class="px-2 py-1 sm:px-3 sm:py-1.5 bg-gradient-to-r from-amber-50 to-amber-100 rounded-lg border border-amber-200">
                <p class="text-[9px] sm:text-xs font-bold text-amber-700">{{ product.karat_display }}</p>
              </div>
            </div>

            <!-- Stock Code Section -->
            <div class="pt-3 sm:pt-4 border-t border-slate-100">
              <div class="flex items-center justify-between">
                <div class="flex-1">
                  <p class="text-[9px] sm:text-xs text-slate-500 mb-1 font-medium">Stok Kodu</p>
                  <div class="text-xs sm:text-sm font-bold text-slate-700">
                    {{ product.stock_code || 'Belirtilmemiş' }}
                  </div>
                </div>
                <div class="p-2 sm:p-2.5 bg-gradient-to-br from-amber-500 to-amber-600 rounded-xl shadow-lg group-hover:shadow-xl group-hover:scale-110 transition-all duration-300">
                  <ShoppingBagIcon class="h-4 w-4 sm:h-5 sm:w-5 text-white" />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import { useRoute } from 'vue-router'
import { StarIcon, ShoppingBagIcon } from '@heroicons/vue/24/outline'
import { useProducts } from '../composables/useProducts'

const route = useRoute()
const { products, isLoading, getAllCategorySlugs, karats, findCategoryBySlug } = useProducts()

const selectedMetalType = ref(null)
const selectedKarat = ref(null)
const sortBy = ref('newest')
const showFilters = ref(false)

const title = computed(() => {
  if (route.params.slug) {
    const category = findCategoryBySlug(route.params.slug)
    return category?.name || 'Ürünler'
  }
  return 'Tüm Ürünler'
})

const filteredProducts = computed(() => {
  if (!Array.isArray(products.value)) return []
  let filtered = products.value

  // Category filter
  if (route.params.slug) {
    const categorySlugs = getAllCategorySlugs(route.params.slug)
    filtered = filtered.filter(p => p.category && categorySlugs.includes(p.category.slug))
  }

  // Metal type filter
  if (selectedMetalType.value) {
    filtered = filtered.filter(p => p.metal_type === selectedMetalType.value)
  }

  // Karat filter
  if (selectedKarat.value) {
    filtered = filtered.filter(p => p.karat === selectedKarat.value)
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

function clearFilters() {
  selectedMetalType.value = null
  selectedKarat.value = null
  sortBy.value = 'newest'
}

// Clear filters and hide filter section when route changes
watch(() => route.params.slug, () => {
  clearFilters()
  showFilters.value = false
})
</script>
