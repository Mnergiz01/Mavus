<template>
  <div
    @click="$emit('click', product)"
    class="product-card-wrapper group/card relative bg-white rounded-2xl overflow-hidden shadow-lg hover:shadow-2xl transition-all duration-500 transform hover:-translate-y-3 border border-slate-100 hover:border-amber-300 cursor-pointer isolate"
  >
    <!-- Glow Effect on Hover -->
    <div class="absolute -inset-1 bg-gradient-to-r from-amber-400 to-amber-600 rounded-2xl blur-xl opacity-0 group-hover/card:opacity-30 transition-opacity duration-500"></div>

    <div class="relative bg-white rounded-2xl overflow-hidden">
      <!-- Media Container (Image/Video Carousel) -->
      <div
        class="aspect-square bg-gradient-to-br from-amber-50 via-white to-slate-50 overflow-hidden relative"
        @mouseenter="playVideoPreview"
        @mouseleave="stopVideoPreview"
      >
        <!-- Main Media Display -->
        <div class="relative w-full h-full">
          <!-- Base Image (always visible) -->
          <img
            v-if="currentImage"
            :src="currentImage"
            :alt="product.name"
            class="w-full h-full object-cover group-hover/card:scale-110 transition-transform duration-700"
          />
          <div v-else class="absolute inset-0 flex items-center justify-center text-6xl opacity-50 group-hover/card:opacity-70 transition-opacity">💎</div>

          <!-- Video Preview on Hover (only first video, only on hover) -->
          <template v-if="hasVideos">
            <video
              ref="videoRef"
              :src="product.videos[0].video"
              class="absolute inset-0 w-full h-full object-cover opacity-0 group-hover/card:opacity-100 transition-opacity duration-500"
              muted
              playsinline
            ></video>
          </template>
        </div>

        <!-- Overlay on Hover -->
        <div class="absolute inset-0 bg-gradient-to-t from-black/50 via-transparent to-transparent opacity-0 group-hover/card:opacity-100 transition-opacity duration-500"></div>

        <!-- Badges -->
        <div class="absolute top-3 left-3 flex flex-col gap-2 z-10">
          <div v-if="showNewBadge" class="bg-gradient-to-r from-emerald-500 to-emerald-600 text-white px-3 py-1.5 rounded-full text-xs font-bold shadow-lg backdrop-blur-sm flex items-center gap-1.5">
            <span class="w-1.5 h-1.5 bg-white rounded-full animate-pulse"></span>
            <span>YENİ</span>
          </div>
          <div v-if="product.is_featured" class="bg-gradient-to-r from-amber-500 to-amber-600 text-white px-3 py-1.5 rounded-full text-xs font-bold shadow-lg backdrop-blur-sm flex items-center gap-1.5">
            <span>⭐</span>
            <span>ÖNE ÇIKAN</span>
          </div>
        </div>

        <!-- Quick View Button (appears on hover) -->
        <div class="absolute inset-0 flex items-center justify-center opacity-0 group-hover/card:opacity-100 transition-all duration-300 pointer-events-none z-20">
          <div class="bg-white/95 backdrop-blur-sm text-amber-600 px-6 py-3 rounded-full font-bold text-sm shadow-xl transform scale-90 group-hover/card:scale-100 transition-transform duration-300 flex items-center gap-2 pointer-events-auto">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
            </svg>
            <span>İncele</span>
          </div>
        </div>
      </div>

      <!-- Content -->
      <div class="p-4 relative">
        <!-- Decorative Line -->
        <div class="absolute top-0 left-1/2 -translate-x-1/2 w-12 h-1 bg-gradient-to-r from-transparent via-amber-400 to-transparent opacity-0 group-hover/card:opacity-100 transition-opacity duration-500"></div>

        <h3 class="text-sm font-bold text-slate-900 mb-2 line-clamp-2 group-hover/card:text-amber-600 transition-colors leading-tight min-h-[2.5rem]">
          {{ product.name }}
        </h3>

        <!-- Product Details -->
        <div class="space-y-2">
          <!-- Stock Code -->
          <div class="flex items-center justify-between text-xs">
            <span class="text-slate-500 font-medium">Stok Kodu:</span>
            <span class="text-slate-700 font-semibold">{{ product.stock_code || 'Belirtilmemiş' }}</span>
          </div>

          <!-- Metal Type -->
          <div v-if="product.metal_type" class="flex items-center justify-between text-xs">
            <span class="text-slate-500 font-medium">Metal:</span>
            <div class="flex items-center gap-1.5">
              <span class="w-2 h-2 rounded-full bg-amber-500"></span>
              <span class="text-slate-700 font-semibold">{{ getMetalTypeName(product.metal_type) }}</span>
            </div>
          </div>

          <!-- Karat -->
          <div v-if="product.karat" class="flex items-center justify-between text-xs">
            <span class="text-slate-500 font-medium">Ayar:</span>
            <span class="bg-amber-50 text-amber-700 px-2.5 py-1 rounded-full font-bold">{{ product.karat }} Ayar</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onUnmounted } from 'vue'

const props = defineProps({
  product: {
    type: Object,
    required: true
  },
  showNewBadge: {
    type: Boolean,
    default: false
  }
})

defineEmits(['click'])

const videoRef = ref(null)
let previewTimeout = null

// Check if product has videos (disabled for now)
const hasVideos = computed(() => {
  return false
})

// Current image to display (main image or first additional image)
const currentImage = computed(() => {
  if (props.product.image) {
    return props.product.image
  }
  if (props.product.images && props.product.images.length > 0) {
    return props.product.images[0].image
  }
  return null
})

// Play video preview (only first 2 seconds)
const playVideoPreview = () => {
  if (videoRef.value) {
    videoRef.value.currentTime = 0
    videoRef.value.play()

    // Stop after 2 seconds and loop
    previewTimeout = setInterval(() => {
      if (videoRef.value && videoRef.value.currentTime >= 2) {
        videoRef.value.currentTime = 0
      }
    }, 100)
  }
}

// Stop video preview
const stopVideoPreview = () => {
  if (previewTimeout) {
    clearInterval(previewTimeout)
    previewTimeout = null
  }
  if (videoRef.value) {
    videoRef.value.pause()
    videoRef.value.currentTime = 0
  }
}

// Cleanup on component unmount
onUnmounted(() => {
  if (previewTimeout) {
    clearInterval(previewTimeout)
  }
})

// Metal tipi için Türkçe isimleri döndür
const getMetalTypeName = (metalType) => {
  const metalTypes = {
    'gold': 'Altın',
    'silver': 'Gümüş',
    'platinum': 'Platin',
    'rose_gold': 'Pembe Altın',
    'white_gold': 'Beyaz Altın',
    'mixed': 'Karma'
  }
  return metalTypes[metalType] || metalType
}
</script>
