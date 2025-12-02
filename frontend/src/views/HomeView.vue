<template>
  <div>
    <!-- Hero Section - Alışverişe Başla -->
    <section class="relative pt-16 overflow-hidden">
      <!-- Large Photo Banner -->
      <div
        class="relative h-[75vh] md:h-[80vh] bg-gradient-to-br from-amber-100 via-amber-50 to-slate-100 flex items-end group/hero"
      >
        <!-- Background Image -->
        <div class="absolute inset-0 w-full h-full">
          <video
            autoplay
            loop
            muted
            playsinline
            class="w-full h-full object-cover"
           src=""
          />
        </div>

        <!-- Dark Overlay for better text readability -->
        <div class="absolute inset-0 bg-black/50"></div>

        <!-- Decorative blur elements (on top of video) -->
        <div class="absolute top-20 left-10 w-96 h-96 bg-amber-400 rounded-full mix-blend-multiply filter blur-3xl opacity-20 animate-blob"></div>
        <div class="absolute top-40 right-10 w-96 h-96 bg-amber-500 rounded-full mix-blend-multiply filter blur-3xl opacity-20 animate-blob animation-delay-2000"></div>

        <!-- Gradient Overlay at bottom -->
        <div class="absolute inset-x-0 bottom-0 h-2/3 bg-gradient-to-t from-slate-900/90 via-slate-900/50 to-transparent"></div>

        <!-- Hero Content at bottom -->
        <div class="relative z-10 container mx-auto px-4 pb-16 md:pb-20">
          <div class="max-w-4xl">
            <h1 class="text-4xl md:text-6xl lg:text-7xl font-serif font-bold text-white mb-4 md:mb-6 animate-fade-in drop-shadow-2xl">
              Zarafet ve Şıklık
              <span class="block text-amber-300 mt-2">Bir Arada</span>
            </h1>

            <p class="text-lg md:text-xl text-white/90 mb-8 max-w-2xl animate-fade-in-up drop-shadow-lg">
              En özel günlerinizi ışıldatacak, benzersiz tasarım kuyum koleksiyonlarımızı keşfedin
            </p>

            <div class="flex animate-fade-in-up">
              <router-link
                to="/products"
                class="px-8 md:px-10 py-4 md:py-5 bg-gradient-to-r from-amber-500 to-amber-600 text-white rounded-2xl font-bold text-base md:text-lg hover:from-amber-400 hover:to-amber-500 transition-all duration-300 shadow-2xl hover:shadow-3xl hover:shadow-amber-500/50 transform hover:scale-105 flex items-center space-x-3"
              >
                <ShoppingBagIcon class="h-5 w-5 md:h-6 md:w-6" />
                <span>Alışverişe Başla</span>
              </router-link>
            </div>
          </div>
        </div>
      </div>

      <!-- Features Bar -->
      <div class="bg-white border-t border-slate-200">
        <div class="container mx-auto px-4 py-8 md:py-12">
          <div class="grid grid-cols-1 md:grid-cols-3 gap-6 md:gap-8">
            <div class="flex items-center space-x-4 p-4 rounded-xl hover:bg-amber-50 transition-all duration-300 group">
              <div class="flex-shrink-0">
                <div class="inline-flex items-center justify-center w-14 h-14 bg-amber-100 rounded-full group-hover:bg-amber-200 transition-colors">
                  <SparklesIcon class="h-7 w-7 text-amber-600" />
                </div>
              </div>
              <div>
                <h3 class="text-lg font-bold text-slate-900 mb-1">Özel Tasarımlar</h3>
                <p class="text-sm text-slate-600">El işçiliği ile hazırlanmış benzersiz modeller</p>
              </div>
            </div>

            <div class="flex items-center space-x-4 p-4 rounded-xl hover:bg-amber-50 transition-all duration-300 group">
              <div class="flex-shrink-0">
                <div class="inline-flex items-center justify-center w-14 h-14 bg-amber-100 rounded-full group-hover:bg-amber-200 transition-colors">
                  <ShieldCheckIcon class="h-7 w-7 text-amber-600" />
                </div>
              </div>
              <div>
                <h3 class="text-lg font-bold text-slate-900 mb-1">Kalite Garantisi</h3>
                <p class="text-sm text-slate-600">Sertifikalı ürünler ve güvenli alışveriş</p>
              </div>
            </div>

            <div class="flex items-center space-x-4 p-4 rounded-xl hover:bg-amber-50 transition-all duration-300 group">
              <div class="flex-shrink-0">
                <div class="inline-flex items-center justify-center w-14 h-14 bg-amber-100 rounded-full group-hover:bg-amber-200 transition-colors">
                  <TruckIcon class="h-7 w-7 text-amber-600" />
                </div>
              </div>
              <div>
                <h3 class="text-lg font-bold text-slate-900 mb-1">Hızlı Teslimat</h3>
                <p class="text-sm text-slate-600">Siparişleriniz özenle paketlenir ve gönderilir</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Best Sellers Section -->
    <section id="best-sellers" class="py-20 bg-white overflow-hidden">
      <div class="container mx-auto px-4">
        <div class="text-center mb-12 animate-fade-in">
          <p class="text-amber-600 text-sm font-bold tracking-widest uppercase mb-3">Popüler Seçimler</p>
          <h2 class="text-4xl md:text-5xl font-serif font-bold text-slate-900 mb-4">
            Çok Satanlar
          </h2>
          <p class="text-lg text-slate-600 max-w-2xl mx-auto">
            En çok tercih edilen ürünlerimiz
          </p>
        </div>

        <!-- Loading State -->
        <div v-if="isLoading" class="text-center py-12">
          <div class="inline-block animate-spin rounded-full h-16 w-16 border-4 border-amber-500 border-t-transparent mb-4"></div>
          <p class="text-slate-600 text-lg">Ürünler yükleniyor...</p>
        </div>

        <!-- No Products -->
        <div v-else-if="bestSellerProducts.length === 0" class="text-center py-12">
          <p class="text-slate-500 text-lg">Henüz çok satan ürün bulunmamaktadır.</p>
        </div>

        <!-- Products -->
        <div v-else class="relative max-w-7xl mx-auto">
          <div class="overflow-hidden">
            <div class="flex gap-4 overflow-x-auto scrollbar-hide snap-x snap-mandatory pb-4">
              <div
                v-for="product in bestSellerProducts"
                :key="product.id"
                class="flex-none w-[47%] sm:w-[31%] md:w-[23%] lg:w-[18%] snap-start"
              >
                <ProductCard :product="product" @click="viewProduct(product)" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- New Products Section -->
    <section id="new-products" class="py-20 bg-gray-50 overflow-hidden">
      <div class="container mx-auto px-4">
        <div class="text-center mb-12 animate-fade-in">
          <p class="text-amber-600 text-sm font-bold tracking-widest uppercase mb-3">Yeni Gelenler</p>
          <h2 class="text-4xl md:text-5xl font-serif font-bold text-slate-900 mb-4">
            Yeni Ürünler
          </h2>
          <p class="text-lg text-slate-600 max-w-2xl mx-auto">
            Son eklenen koleksiyonlarımızı keşfedin
          </p>
        </div>

        <!-- Loading State -->
        <div v-if="isLoading" class="text-center py-12">
          <div class="inline-block animate-spin rounded-full h-16 w-16 border-4 border-amber-500 border-t-transparent mb-4"></div>
          <p class="text-slate-600 text-lg">Ürünler yükleniyor...</p>
        </div>

        <!-- No Products -->
        <div v-else-if="products.length === 0" class="text-center py-12">
          <p class="text-slate-500 text-lg">Henüz ürün bulunmamaktadır.</p>
        </div>

        <!-- Products -->
        <div v-else class="relative max-w-7xl mx-auto">
          <div class="overflow-hidden">
            <div class="flex gap-4 overflow-x-auto scrollbar-hide snap-x snap-mandatory pb-4">
              <div
                v-for="product in products.slice(0, 8)"
                :key="'new-' + product.id"
                class="flex-none w-[47%] sm:w-[31%] md:w-[23%] lg:w-[18%] snap-start"
              >
                <ProductCard :product="product" :show-new-badge="true" @click="viewProduct(product)" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Recommended Products Section -->
    <section id="recommended-products" class="py-20 bg-white overflow-hidden">
      <div class="container mx-auto px-4">
        <div class="text-center mb-12 animate-fade-in">
          <p class="text-amber-600 text-sm font-bold tracking-widest uppercase mb-3">Size Özel</p>
          <h2 class="text-4xl md:text-5xl font-serif font-bold text-slate-900 mb-4">
            İlginizi Çekebilecek Ürünler
          </h2>
          <p class="text-lg text-slate-600 max-w-2xl mx-auto">
            Sizin için seçtiğimiz özel ürünler
          </p>
        </div>

        <!-- Loading State -->
        <div v-if="isLoading" class="text-center py-12">
          <div class="inline-block animate-spin rounded-full h-16 w-16 border-4 border-amber-500 border-t-transparent mb-4"></div>
          <p class="text-slate-600 text-lg">Ürünler yükleniyor...</p>
        </div>

        <!-- No Products -->
        <div v-else-if="recommendedProducts.length === 0" class="text-center py-12">
          <p class="text-slate-500 text-lg">Henüz önerilen ürün bulunmamaktadır.</p>
        </div>

        <!-- Products -->
        <div v-else class="relative max-w-7xl mx-auto">
          <div class="overflow-hidden">
            <div class="flex gap-4 overflow-x-auto scrollbar-hide snap-x snap-mandatory pb-4">
              <div
                v-for="product in recommendedProducts"
                :key="'rec-' + product.id"
                class="flex-none w-[47%] sm:w-[31%] md:w-[23%] lg:w-[18%] snap-start"
              >
                <ProductCard :product="product" @click="viewProduct(product)" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Live Gold Prices Section -->
    <section class="py-16 bg-gradient-to-br from-slate-900 via-slate-800 to-amber-900 relative overflow-hidden">
      <!-- Decorative Elements -->
      <div class="absolute inset-0 opacity-10">
        <div class="absolute top-10 left-10 w-72 h-72 bg-amber-500 rounded-full blur-3xl animate-pulse"></div>
        <div class="absolute bottom-10 right-10 w-72 h-72 bg-amber-400 rounded-full blur-3xl animate-pulse animation-delay-2000"></div>
      </div>

      <div class="container mx-auto px-4 relative z-10">
        <div class="text-center mb-10">
          <div class="inline-flex items-center justify-center space-x-2 mb-4">
            <div class="w-3 h-3 bg-green-400 rounded-full animate-pulse"></div>
            <span class="text-green-400 text-sm font-bold tracking-wider uppercase">Canlı Veriler</span>
          </div>
          <h2 class="text-3xl md:text-4xl font-serif font-bold text-white mb-3">
            Anlık Altın ve Döviz Kurları
          </h2>
          <p class="text-slate-300 text-lg">
            Haremaltin.com'dan anlık olarak güncellenen fiyatlar
          </p>
        </div>

        <div v-if="exchangeRates" class="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-5xl mx-auto">
          <!-- Gold Price Card -->
          <div v-if="exchangeRates.GOLD" class="group relative bg-gradient-to-br from-amber-500/20 to-amber-600/20 backdrop-blur-sm border border-amber-500/30 rounded-2xl p-6 hover:scale-105 transition-all duration-300 hover:shadow-2xl hover:shadow-amber-500/30">
            <div class="absolute inset-0 bg-gradient-to-br from-amber-400/0 to-amber-600/10 rounded-2xl opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
            <div class="relative z-10">
              <div class="flex items-center justify-between mb-4">
                <div class="flex items-center space-x-3">
                  <div class="w-12 h-12 bg-amber-500/30 rounded-xl flex items-center justify-center group-hover:bg-amber-500/50 transition-colors">
                    <span class="text-2xl">⚜️</span>
                  </div>
                  <div>
                    <p class="text-amber-300 text-xs font-medium uppercase tracking-wider">Altın</p>
                    <p class="text-white text-lg font-bold">{{ exchangeRates.GOLD.name }}</p>
                  </div>
                </div>
              </div>

              <div class="space-y-3">
                <div class="bg-white/5 backdrop-blur-sm rounded-xl p-3 border border-white/10">
                  <p class="text-amber-200 text-xs font-medium mb-1 uppercase">Alış</p>
                  <p class="text-white text-2xl font-bold">{{ exchangeRates.GOLD.buying.toFixed(2) }} <span class="text-lg">₺</span></p>
                </div>
                <div class="bg-white/5 backdrop-blur-sm rounded-xl p-3 border border-white/10">
                  <p class="text-amber-200 text-xs font-medium mb-1 uppercase">Satış</p>
                  <p class="text-white text-2xl font-bold">{{ exchangeRates.GOLD.selling.toFixed(2) }} <span class="text-lg">₺</span></p>
                </div>
              </div>
            </div>
          </div>

          <!-- USD Price Card -->
          <div v-if="exchangeRates.USD" class="group relative bg-gradient-to-br from-green-500/20 to-green-600/20 backdrop-blur-sm border border-green-500/30 rounded-2xl p-6 hover:scale-105 transition-all duration-300 hover:shadow-2xl hover:shadow-green-500/30">
            <div class="absolute inset-0 bg-gradient-to-br from-green-400/0 to-green-600/10 rounded-2xl opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
            <div class="relative z-10">
              <div class="flex items-center justify-between mb-4">
                <div class="flex items-center space-x-3">
                  <div class="w-12 h-12 bg-green-500/30 rounded-xl flex items-center justify-center group-hover:bg-green-500/50 transition-colors">
                    <span class="text-2xl">💵</span>
                  </div>
                  <div>
                    <p class="text-green-300 text-xs font-medium uppercase tracking-wider">Döviz</p>
                    <p class="text-white text-lg font-bold">{{ exchangeRates.USD.name }}</p>
                  </div>
                </div>
              </div>

              <div class="space-y-3">
                <div class="bg-white/5 backdrop-blur-sm rounded-xl p-3 border border-white/10">
                  <p class="text-green-200 text-xs font-medium mb-1 uppercase">Alış</p>
                  <p class="text-white text-2xl font-bold">{{ exchangeRates.USD.buying.toFixed(2) }} <span class="text-lg">₺</span></p>
                </div>
                <div class="bg-white/5 backdrop-blur-sm rounded-xl p-3 border border-white/10">
                  <p class="text-green-200 text-xs font-medium mb-1 uppercase">Satış</p>
                  <p class="text-white text-2xl font-bold">{{ exchangeRates.USD.selling.toFixed(2) }} <span class="text-lg">₺</span></p>
                </div>
              </div>
            </div>
          </div>

          <!-- EUR Price Card -->
          <div v-if="exchangeRates.EUR" class="group relative bg-gradient-to-br from-blue-500/20 to-blue-600/20 backdrop-blur-sm border border-blue-500/30 rounded-2xl p-6 hover:scale-105 transition-all duration-300 hover:shadow-2xl hover:shadow-blue-500/30">
            <div class="absolute inset-0 bg-gradient-to-br from-blue-400/0 to-blue-600/10 rounded-2xl opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
            <div class="relative z-10">
              <div class="flex items-center justify-between mb-4">
                <div class="flex items-center space-x-3">
                  <div class="w-12 h-12 bg-blue-500/30 rounded-xl flex items-center justify-center group-hover:bg-blue-500/50 transition-colors">
                    <span class="text-2xl">💶</span>
                  </div>
                  <div>
                    <p class="text-blue-300 text-xs font-medium uppercase tracking-wider">Döviz</p>
                    <p class="text-white text-lg font-bold">{{ exchangeRates.EUR.name }}</p>
                  </div>
                </div>
              </div>

              <div class="space-y-3">
                <div class="bg-white/5 backdrop-blur-sm rounded-xl p-3 border border-white/10">
                  <p class="text-blue-200 text-xs font-medium mb-1 uppercase">Alış</p>
                  <p class="text-white text-2xl font-bold">{{ exchangeRates.EUR.buying.toFixed(2) }} <span class="text-lg">₺</span></p>
                </div>
                <div class="bg-white/5 backdrop-blur-sm rounded-xl p-3 border border-white/10">
                  <p class="text-blue-200 text-xs font-medium mb-1 uppercase">Satış</p>
                  <p class="text-white text-2xl font-bold">{{ exchangeRates.EUR.selling.toFixed(2) }} <span class="text-lg">₺</span></p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Loading State -->
        <div v-else class="text-center text-white">
          <div class="inline-block animate-spin rounded-full h-12 w-12 border-4 border-amber-500 border-t-transparent mb-4"></div>
          <p class="text-lg">Fiyatlar yükleniyor...</p>
        </div>

        <!-- Update Info -->
        <div class="text-center mt-8">
          <p class="text-slate-400 text-sm">
            <span class="inline-flex items-center space-x-2">
              <span class="w-2 h-2 bg-green-400 rounded-full animate-pulse"></span>
              <span>Fiyatlar her 5 dakikada bir otomatik güncellenir</span>
            </span>
          </p>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { ShoppingBagIcon, SparklesIcon, ShieldCheckIcon, TruckIcon } from '@heroicons/vue/24/outline'
import { useProducts } from '../composables/useProducts'
import { useExchangeRates } from '../composables/useExchangeRates'
import ProductCard from '../components/ProductCard.vue'

const router = useRouter()
const { products, bestSellerProducts, recommendedProducts, isLoading } = useProducts()
const { exchangeRates } = useExchangeRates()

function viewProduct(product) {
  router.push(`/products/${product.slug}`)
}
</script>
