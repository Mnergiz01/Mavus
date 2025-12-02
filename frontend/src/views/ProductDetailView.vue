<template>
  <div class="pt-32 pb-20 bg-white">
    <div class="container mx-auto px-4">
      <button
        @click="$router.back()"
        class="mb-8 flex items-center space-x-2 text-slate-600 hover:text-amber-600 font-semibold transition-colors group"
      >
        <svg class="h-5 w-5 group-hover:-translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/>
        </svg>
        <span>Geri Dön</span>
      </button>

      <div v-if="!product" class="text-center py-20">
        <div class="inline-block animate-spin rounded-full h-16 w-16 border-4 border-amber-500 border-t-transparent mb-4"></div>
        <p class="text-slate-600 text-lg">Yükleniyor...</p>
      </div>

      <div v-else class="grid grid-cols-1 lg:grid-cols-2 gap-12 max-w-7xl mx-auto">
        <!-- Product Images & Videos Gallery -->
        <div class="space-y-4">
          <!-- Main Display -->
          <div class="relative aspect-square bg-gradient-to-br from-amber-50 to-slate-100 rounded-3xl overflow-hidden shadow-2xl group">
            <template v-if="allImages.length > 0">
              <template v-if="allImages[selectedImageIndex].type === 'video'">
                <video
                  :src="allImages[selectedImageIndex].url"
                  class="w-full h-full object-cover"
                  controls
                  autoplay
                  loop
                  muted
                ></video>
                <div class="absolute top-6 left-6 bg-gradient-to-r from-purple-500 to-purple-600 text-white px-4 py-2 rounded-full text-xs font-bold tracking-wider shadow-xl flex items-center space-x-2">
                  <PlayIcon class="h-4 w-4" />
                  <span>VİDEO</span>
                </div>
              </template>
              <template v-else>
                <img
                  :src="allImages[selectedImageIndex].url"
                  :alt="allImages[selectedImageIndex].alt"
                  class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700"
                />
              </template>
            </template>
            <div v-else class="absolute inset-0 flex items-center justify-center text-9xl">💎</div>

            <!-- Featured Badge -->
            <div v-if="product.is_featured" class="absolute top-6 right-6 bg-gradient-to-r from-amber-500 to-amber-600 text-white px-5 py-2 rounded-full text-sm font-bold tracking-wider shadow-xl flex items-center space-x-2">
              <StarIcon class="h-5 w-5" />
              <span>ÖZEL PARÇA</span>
            </div>

            <!-- Navigation Arrows (only show if multiple images/videos) -->
            <template v-if="allImages.length > 1">
              <button
                @click="prevImage"
                class="absolute left-4 top-1/2 -translate-y-1/2 bg-white/90 hover:bg-white text-slate-900 p-3 rounded-full shadow-xl opacity-0 group-hover:opacity-100 transition-all duration-300 hover:scale-110"
              >
                <ChevronLeftIcon class="h-5 w-5" />
              </button>
              <button
                @click="nextImage"
                class="absolute right-4 top-1/2 -translate-y-1/2 bg-white/90 hover:bg-white text-slate-900 p-3 rounded-full shadow-xl opacity-0 group-hover:opacity-100 transition-all duration-300 hover:scale-110"
              >
                <ChevronRightIcon class="h-5 w-5" />
              </button>

              <!-- Image Counter -->
              <div class="absolute bottom-4 left-1/2 transform -translate-x-1/2 bg-black/60 backdrop-blur-sm text-white px-4 py-2 rounded-full text-sm font-medium">
                {{ selectedImageIndex + 1 }} / {{ allImages.length }}
              </div>
            </template>
          </div>

          <!-- Thumbnail Gallery -->
          <div v-if="allImages.length > 1" class="grid grid-cols-5 gap-3">
            <div
              v-for="(media, index) in allImages"
              :key="index"
              @click="selectedImageIndex = index"
              :class="[
                'relative aspect-square bg-gradient-to-br from-amber-50 to-slate-100 rounded-xl overflow-hidden cursor-pointer transition-all duration-300',
                index === selectedImageIndex
                  ? 'ring-4 ring-amber-500 scale-105'
                  : 'hover:ring-4 hover:ring-amber-300 opacity-70 hover:opacity-100'
              ]"
            >
              <template v-if="media.type === 'video'">
                <video
                  :src="media.url"
                  class="w-full h-full object-cover"
                  muted
                ></video>
                <div class="absolute inset-0 flex items-center justify-center bg-black/30">
                  <PlayIcon class="h-8 w-8 text-white" />
                </div>
              </template>
              <template v-else>
                <img
                  :src="media.url"
                  :alt="media.alt"
                  class="w-full h-full object-cover"
                />
              </template>
            </div>
          </div>
        </div>

        <!-- Product Details -->
        <div class="flex flex-col">
          <div class="mb-6">
            <p class="text-amber-600 text-sm font-bold tracking-widest uppercase mb-3">{{ product.category.name }}</p>
            <h1 class="text-5xl font-serif font-bold text-slate-900 mb-6 leading-tight">
              {{ product.name }}
            </h1>
            <p class="text-lg text-slate-600 leading-relaxed">
              {{ product.description }}
            </p>
          </div>

          <!-- Specifications -->
          <div class="bg-gradient-to-br from-slate-50 to-amber-50/30 rounded-2xl p-8 mb-8 space-y-4">
            <h3 class="text-xl font-serif font-bold text-slate-900 mb-6">Ürün Özellikleri</h3>

            <div class="grid grid-cols-2 gap-6">
              <div class="space-y-2">
                <p class="text-sm text-slate-500 uppercase tracking-wider">Metal</p>
                <p class="text-lg font-semibold text-slate-900">{{ product.metal_type_display }}</p>
              </div>

              <div v-if="product.karat" class="space-y-2">
                <p class="text-sm text-slate-500 uppercase tracking-wider">Ayar</p>
                <p class="text-lg font-semibold text-slate-900">{{ product.karat_display }}</p>
              </div>

              <div class="space-y-2">
                <p class="text-sm text-slate-500 uppercase tracking-wider">Ağırlık</p>
                <p class="text-lg font-semibold text-slate-900">{{ product.weight }} gram</p>
              </div>

              <div class="space-y-2">
                <p class="text-sm text-slate-500 uppercase tracking-wider">Stok Kodu</p>
                <p class="text-lg font-semibold text-amber-600">
                  {{ product.stock_code || 'Belirtilmemiş' }}
                </p>
              </div>
            </div>
          </div>

          <!-- CTA Button -->
          <div class="mt-auto space-y-4">
            <a
              :href="whatsappLink"
              target="_blank"
              class="w-full px-8 py-4 bg-gradient-to-r from-green-600 to-green-500 text-white rounded-xl font-bold text-lg hover:from-green-500 hover:to-green-600 transition-all duration-300 shadow-lg hover:shadow-green-500/50 transform hover:-translate-y-1 flex items-center justify-center space-x-2"
            >
              <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg>
              <span>WhatsApp ile İletişime Geç</span>
            </a>
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

      <!-- Related Products from Same Category -->
      <div v-if="product && relatedProducts.length > 0" class="mt-20">
        <div class="text-center mb-12">
          <h2 class="text-3xl font-serif font-bold text-slate-900 mb-3 animate-fade-in">Kategorinin Diğer Ürünleri</h2>
          <div class="w-24 h-1 bg-gradient-to-r from-amber-400 to-amber-600 mx-auto rounded-full"></div>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-6 max-w-7xl mx-auto">
          <ProductCard
            v-for="relProduct in relatedProducts"
            :key="relProduct.id"
            :product="relProduct"
            @click="$router.push(`/products/${relProduct.slug}`)"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import { useRoute } from 'vue-router'
import { StarIcon, ShieldCheckIcon, TruckIcon, ChevronLeftIcon, ChevronRightIcon, PlayIcon } from '@heroicons/vue/24/outline'
import { useProducts } from '../composables/useProducts'
import ProductCard from '../components/ProductCard.vue'

const route = useRoute()
const { products, findProductBySlug } = useProducts()

const selectedImageIndex = ref(0)

const product = computed(() => {
  return findProductBySlug(route.params.slug)
})

const allImages = computed(() => {
  if (!product.value) return []
  const images = []

  // Ana görsel
  if (product.value.image) {
    images.push({ url: product.value.image, type: 'image', alt: product.value.name })
  }

  // Ek görseller ve videolar
  if (product.value.images && product.value.images.length > 0) {
    product.value.images.forEach(img => {
      images.push({
        url: img.image,
        type: img.is_video ? 'video' : 'image',
        alt: img.alt_text || product.value.name
      })
    })
  }

  return images
})

const relatedProducts = computed(() => {
  if (!product.value) return []

  return products.value
    .filter(p => p.category.slug === product.value.category.slug && p.id !== product.value.id)
    .slice(0, 4)
})

const whatsappLink = computed(() => {
  if (!product.value) return ''

  const message = `Merhaba! ${product.value.name} ürünü hakkında bilgi almak istiyorum.%0A%0AStok Kodu: ${product.value.stock_code || 'Belirtilmemiş'}%0AÜrün Linki: ${window.location.href}`

  return `https://wa.me/905452409490?text=${message}`
})

function nextImage() {
  selectedImageIndex.value = (selectedImageIndex.value + 1) % allImages.value.length
}

function prevImage() {
  selectedImageIndex.value = selectedImageIndex.value === 0
    ? allImages.value.length - 1
    : selectedImageIndex.value - 1
}

// Reset image index when product changes
watch(() => route.params.slug, () => {
  selectedImageIndex.value = 0
})
</script>
