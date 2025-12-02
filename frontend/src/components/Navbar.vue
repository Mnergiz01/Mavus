<template>
  <!-- Clean Header -->
  <header
    class="fixed top-0 left-0 right-0 z-50 bg-white border-b border-gray-200 transition-all duration-300"
    :class="scrolled ? 'shadow-md' : ''"
  >
    <div class="container mx-auto px-4 lg:px-6 py-4">
      <div class="flex items-center justify-between">
        <!-- Logo -->
        <router-link to="/" class="flex items-center cursor-pointer group">
          <div class="relative px-4 py-2">
            <!-- Glow Effect -->
            <div class="absolute inset-0 bg-gradient-to-r from-amber-400 via-yellow-400 to-amber-500 rounded-lg blur-xl opacity-0 group-hover:opacity-40 transition-all duration-500"></div>

            <!-- Decorative Border -->
            <div class="absolute inset-0 border-2 border-transparent group-hover:border-amber-400/30 rounded-lg transition-all duration-300"></div>

            <div class="relative">
              <!-- Main Brand Name with Luxury Styling -->
              <div class="flex items-center gap-2 mb-1">
                
                <h1 class="text-3xl font-serif font-black tracking-[0.15em] bg-gradient-to-r from-amber-700 via-amber-500 to-amber-700 bg-clip-text text-transparent drop-shadow-sm">
                  MAWUŞ
                </h1>
                
              </div>

              <!-- Decorative Line -->
              <div class="flex items-center justify-center gap-1 mb-0.5">
                <div class="w-8 h-px bg-gradient-to-r from-transparent via-amber-500 to-transparent"></div>
                <div class="w-1 h-1 bg-amber-500 rounded-full"></div>
                <div class="w-8 h-px bg-gradient-to-r from-transparent via-amber-500 to-transparent"></div>
              </div>

              <!-- Subtitle with Elegant Spacing -->
              <p class="text-[9px] tracking-[0.35em] uppercase text-amber-700 font-bold text-center">
                KUYUMCULUK
              </p>

              <!-- Premium Badge (appears on hover) -->
              <div class="absolute -top-2 -right-2 opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                <div class="w-2 h-2 bg-amber-500 rounded-full animate-pulse"></div>
              </div>
            </div>
          </div>
        </router-link>

        <!-- Mobile menu button -->
        <button
          @click="showMobileMenu = !showMobileMenu"
          class="md:hidden p-2 rounded-lg text-gray-700 hover:bg-gray-100 transition-colors"
        >
          <Bars3Icon v-if="!showMobileMenu" class="h-6 w-6" />
          <XMarkIcon v-else class="h-6 w-6" />
        </button>

        <!-- Desktop Navigation -->
        <nav class="hidden md:flex items-center space-x-6">
          <router-link
            to="/#best-sellers"
            class="text-gray-700 hover:text-amber-600 font-medium text-sm transition-colors"
          >
            Çok Satanlar
          </router-link>

          <router-link
            to="/#new-products"
            class="text-gray-700 hover:text-amber-600 font-medium text-sm transition-colors"
          >
            Yeni Ürünler
          </router-link>

          <router-link
            to="/#recommended-products"
            class="text-gray-700 hover:text-amber-600 font-medium text-sm transition-colors"
          >
            İlginizi Çekebilecek Ürünler
          </router-link>

          <!-- Category Dropdowns -->
          <div
            v-for="category in parentCategories"
            :key="category.id"
            class="relative group"
          >
            <button
              @click="$router.push(`/products/category/${category.slug}`); hoveredCategory = null"
              @mouseenter="hoveredCategory = category.id"
              :class="[
                'flex items-center space-x-1 font-medium text-sm transition-all duration-200 py-2 px-3 rounded-lg',
                hoveredCategory === category.id ? 'text-amber-600 bg-amber-50' : 'text-gray-700 hover:text-amber-600 hover:bg-gray-50'
              ]"
            >
              <span>{{ category.name }}</span>
              <ChevronDownIcon
                v-if="category.children && category.children.length > 0"
                :class="[
                  'h-4 w-4 transition-transform duration-300',
                  hoveredCategory === category.id ? 'rotate-180' : ''
                ]"
              />
            </button>

            <!-- Modern Dropdown Menu with Images - Single Row -->
            <div
              v-if="hoveredCategory === category.id && category.children && category.children.length > 0"
              @mouseenter="hoveredCategory = category.id"
              @mouseleave="hoveredCategory = null"
              class="absolute top-full left-1/2 -translate-x-1/2 bg-white rounded-2xl shadow-2xl border border-amber-200/50 overflow-hidden z-50 dropdown-menu"
              style="min-width: 650px; max-width: 90vw; margin-top: 12px;"
            >
              <!-- Decorative Top Border -->
              <div class="h-1 bg-gradient-to-r from-amber-400 via-amber-500 to-amber-600"></div>

              <!-- Dropdown Header -->
              <div class="relative bg-gradient-to-br from-amber-500 via-amber-600 to-amber-700 px-6 py-4 overflow-hidden">
                <!-- Background Pattern -->
                <div class="absolute inset-0 opacity-10">
                  <div class="absolute top-0 right-0 w-32 h-32 bg-white rounded-full blur-2xl"></div>
                  <div class="absolute bottom-0 left-0 w-24 h-24 bg-white rounded-full blur-2xl"></div>
                </div>

                <div class="relative z-10 flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <div class="w-10 h-10 bg-white/20 rounded-xl backdrop-blur-sm flex items-center justify-center">
                      <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
                      </svg>
                    </div>
                    <div>
                      <h3 class="text-white font-bold text-lg">{{ category.name }}</h3>
                      <p class="text-amber-100 text-xs font-medium">{{ category.children.length }} Kategori Mevcut</p>
                    </div>
                  </div>
                  <button
                    @click="$router.push(`/products/category/${category.slug}`); hoveredCategory = null"
                    class="flex items-center gap-2 px-4 py-2 bg-white/20 hover:bg-white/30 backdrop-blur-sm text-white rounded-lg text-sm font-semibold transition-all duration-300 hover:scale-105"
                  >
                    <span>Tümünü Gör</span>
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6" />
                    </svg>
                  </button>
                </div>
              </div>

              <!-- Subcategories Horizontal Scroll -->
              <div class="p-5 bg-gradient-to-b from-gray-50 to-white">
                <div class="overflow-x-auto scrollbar-hide">
                  <div class="flex gap-4 pb-2" style="width: max-content;">
                    <button
                      v-for="(child, index) in category.children"
                      :key="child.id"
                      @click="$router.push(`/products/category/${child.slug}`); hoveredCategory = null"
                      class="group/item relative overflow-hidden rounded-2xl bg-white border-2 border-gray-200 hover:border-amber-400 transition-all duration-300 hover:shadow-2xl hover:-translate-y-1 flex-shrink-0 category-card"
                      :style="`width: 150px; animation: slideInFromBottom 0.4s ease-out ${index * 0.05}s backwards;`"
                    >
                      <!-- Category Image -->
                      <div class="aspect-square overflow-hidden bg-gradient-to-br from-amber-50 via-gray-50 to-slate-50 relative">
                        <img
                          v-if="child.image"
                          :src="child.image"
                          :alt="child.name"
                          class="w-full h-full object-cover group-hover/item:scale-110 transition-transform duration-700 ease-out"
                        />
                        <div v-else class="w-full h-full flex items-center justify-center text-5xl opacity-30 group-hover/item:opacity-50 transition-opacity">
                          💎
                        </div>

                        <!-- Gradient Overlay -->
                        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/30 to-transparent opacity-0 group-hover/item:opacity-100 transition-all duration-400"></div>

                        <!-- Hover Badge -->
                        <div class="absolute inset-0 flex items-center justify-center opacity-0 group-hover/item:opacity-100 transition-all duration-300 transform scale-75 group-hover/item:scale-100">
                          <div class="bg-gradient-to-r from-amber-500 to-amber-600 text-white px-4 py-2 rounded-full font-bold text-xs shadow-2xl flex items-center gap-2">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                            </svg>
                            <span>İncele</span>
                          </div>
                        </div>

                        <!-- Shimmer Effect -->
                        <div class="absolute inset-0 opacity-0 group-hover/item:opacity-100 transition-opacity duration-500">
                          <div class="absolute inset-0 bg-gradient-to-r from-transparent via-white/20 to-transparent shimmer"></div>
                        </div>
                      </div>

                      <!-- Category Name -->
                      <div class="p-3 bg-gradient-to-b from-white to-gray-50 group-hover/item:from-amber-50 group-hover/item:to-amber-100/50 transition-colors duration-300">
                        <h4 class="text-xs font-bold text-slate-900 group-hover/item:text-amber-700 transition-colors text-center leading-tight line-clamp-2 min-h-[2rem] flex items-center justify-center">
                          {{ child.name }}
                        </h4>
                      </div>

                      <!-- Glow Effect -->
                      <div class="absolute -inset-1 bg-gradient-to-r from-amber-400 via-amber-500 to-amber-600 rounded-2xl blur-lg opacity-0 group-hover/item:opacity-40 transition-all duration-500 -z-10"></div>
                    </button>
                  </div>
                </div>
              </div>

              <!-- Bottom Decoration -->
              <div class="h-1 bg-gradient-to-r from-amber-600 via-amber-500 to-amber-400 opacity-50"></div>
            </div>
          </div>

          <!-- About Link -->
          <router-link
            to="/about"
            class="text-gray-700 hover:text-amber-600 font-medium text-sm transition-colors"
          >
            Hakkımızda
          </router-link>
        </nav>
      </div>

      <!-- Mobile Sidebar Overlay -->
      <div
        v-if="showMobileMenu"
        @click="showMobileMenu = false"
        class="md:hidden fixed inset-0 bg-black/60 backdrop-blur-sm z-40 transition-opacity duration-300"
      ></div>

      <!-- Mobile Sidebar -->
      <nav
        :class="[
          'md:hidden fixed top-0 right-0 h-full w-80 bg-white shadow-2xl z-50 transform transition-transform duration-300 ease-out overflow-y-auto',
          showMobileMenu ? 'translate-x-0' : 'translate-x-full'
        ]"
      >
        <!-- Sidebar Header -->
        <div class="flex items-center justify-between p-6 border-b border-gray-200 bg-gradient-to-r from-amber-50 to-white">
          <div class="flex items-center">
            <div class="relative px-3 py-2">
              <div class="relative">
                <!-- Main Brand Name -->
                <div class="flex items-center gap-1.5 mb-1">
                  <div class="w-0.5 h-5 bg-gradient-to-b from-amber-600 via-amber-500 to-amber-400 rounded-full"></div>
                  <h1 class="text-2xl font-serif font-black tracking-[0.15em] bg-gradient-to-r from-amber-700 via-amber-500 to-amber-700 bg-clip-text text-transparent">
                    MAVUŞ
                  </h1>
                  <div class="w-0.5 h-5 bg-gradient-to-b from-amber-400 via-amber-500 to-amber-600 rounded-full"></div>
                </div>

                <!-- Decorative Line -->
                <div class="flex items-center justify-center gap-1 mb-0.5">
                  <div class="w-6 h-px bg-gradient-to-r from-transparent via-amber-500 to-transparent"></div>
                  <div class="w-0.5 h-0.5 bg-amber-500 rounded-full"></div>
                  <div class="w-6 h-px bg-gradient-to-r from-transparent via-amber-500 to-transparent"></div>
                </div>

                <!-- Subtitle -->
                <p class="text-[7px] tracking-[0.35em] uppercase text-amber-700 font-bold text-center">
                  KUYUMCULUK
                </p>
              </div>
            </div>
          </div>
          <button
            @click="showMobileMenu = false"
            class="p-2 rounded-lg text-gray-700 hover:bg-gray-100 transition-colors"
          >
            <XMarkIcon class="h-6 w-6" />
          </button>
        </div>

        <!-- Sidebar Content -->
        <div class="p-4 space-y-2">
          <!-- Best Sellers -->
          <router-link
            to="/#best-sellers"
            @click="showMobileMenu = false"
            class="flex items-center space-x-3 px-4 py-3 rounded-lg font-medium text-gray-700 hover:bg-gray-50 transition-all duration-300 w-full"
          >
            <StarIcon class="h-5 w-5 text-amber-600" />
            <span>Çok Satanlar</span>
          </router-link>

          <!-- New Products -->
          <router-link
            to="/#new-products"
            @click="showMobileMenu = false"
            class="flex items-center space-x-3 px-4 py-3 rounded-lg font-medium text-gray-700 hover:bg-gray-50 transition-all duration-300 w-full"
          >
            <SparklesIcon class="h-5 w-5 text-amber-600" />
            <span>Yeni Ürünler</span>
          </router-link>

          <!-- Recommended Products -->
          <router-link
            to="/#recommended-products"
            @click="showMobileMenu = false"
            class="flex items-center space-x-3 px-4 py-3 rounded-lg font-medium text-gray-700 hover:bg-gray-50 transition-all duration-300 w-full"
          >
            <SparklesIcon class="h-5 w-5 text-amber-600" />
            <span>İlginizi Çekebilecek</span>
          </router-link>

          <!-- Collections Accordion -->
          <div>
            <button
              @click="showCollectionsMenu = !showCollectionsMenu"
              class="flex items-center justify-between w-full px-4 py-3 rounded-lg font-medium text-gray-700 hover:bg-gray-50 transition-all duration-300"
            >
              <div class="flex items-center space-x-3">
                <ShoppingBagIcon class="h-5 w-5 text-amber-600" />
                <span>Koleksiyonlar</span>
              </div>
              <ChevronDownIcon
                :class="[
                  'h-5 w-5 text-gray-500 transition-transform duration-300',
                  showCollectionsMenu ? 'rotate-180' : ''
                ]"
              />
            </button>

            <!-- Collections Submenu -->
            <div
              :class="[
                'overflow-hidden transition-all duration-300',
                showCollectionsMenu ? 'max-h-[1000px] opacity-100' : 'max-h-0 opacity-0'
              ]"
            >
              <div class="ml-4 mt-2 space-y-2">
                <!-- Parent Categories -->
                <div v-for="category in parentCategories" :key="category.id" class="space-y-1">
                  <!-- Parent Category Button -->
                  <div class="flex items-center space-x-1">
                    <button
                      v-if="category.children && category.children.length > 0"
                      @click="toggleParentCategory(category.id)"
                      class="p-1 hover:bg-gray-100 rounded transition-colors"
                    >
                      <ChevronDownIcon
                        :class="[
                          'h-4 w-4 text-amber-600 transition-transform duration-300',
                          !!openParentCategories[category.id] ? 'rotate-180' : ''
                        ]"
                      />
                    </button>
                    <button
                      @click="$router.push(`/products/category/${category.slug}`); showMobileMenu = false"
                      class="flex-1 text-left px-3 py-2 rounded-lg text-sm font-semibold text-amber-600 hover:bg-gray-50 transition-all duration-300"
                    >
                      {{ category.name }}
                    </button>
                  </div>

                  <!-- Child Categories (Subcategories) -->
                  <div
                    v-if="category.children && category.children.length > 0"
                    :class="[
                      'overflow-hidden transition-all duration-300 ml-6',
                      !!openParentCategories[category.id] ? 'max-h-96 opacity-100' : 'max-h-0 opacity-0'
                    ]"
                  >
                    <div class="space-y-1 border-l-2 border-amber-200 pl-3">
                      <button
                        v-for="child in category.children"
                        :key="child.id"
                        @click="$router.push(`/products/category/${child.slug}`); showMobileMenu = false"
                        class="block w-full text-left px-3 py-1.5 rounded-lg text-sm text-gray-600 hover:text-amber-600 hover:bg-gray-50 transition-all duration-300"
                      >
                        {{ child.name }}
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- About -->
          <router-link
            to="/about"
            @click="showMobileMenu = false"
            class="flex items-center space-x-3 px-4 py-3 rounded-lg font-medium text-gray-700 hover:bg-gray-50 transition-all duration-300 w-full"
          >
            <SparklesIcon class="h-5 w-5 text-amber-600" />
            <span>Hakkımızda</span>
          </router-link>

          <!-- Divider -->
          <div class="border-t border-gray-200 my-4"></div>

          <!-- Admin Panel -->
          <a
            href="http://127.0.0.1:8000/admin/"
            target="_blank"
            class="flex items-center justify-center space-x-2 px-4 py-3 bg-amber-600 text-white rounded-lg font-semibold transition-all duration-300 hover:bg-amber-700"
          >
            <ShieldCheckIcon class="h-5 w-5" />
            <span>Admin Panel</span>
          </a>
        </div>
      </nav>
    </div>
  </header>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import {
  Bars3Icon,
  XMarkIcon,
  ChevronDownIcon,
  ShoppingBagIcon,
  StarIcon,
  ShieldCheckIcon
} from '@heroicons/vue/24/outline'
import { useProducts } from '../composables/useProducts'

const { parentCategories } = useProducts()

const showMobileMenu = ref(false)
const scrolled = ref(false)
const hoveredCategory = ref(null)
const showCollectionsMenu = ref(false)
const openParentCategories = ref({})

function handleScroll() {
  // window nesnesinin yalnızca istemci tarafında mevcut olduğundan emin olun
  if (typeof window !== 'undefined') {
    scrolled.value = window.scrollY > 50
  }
}

function toggleParentCategory(categoryId) {
  openParentCategories.value[categoryId] = !openParentCategories.value[categoryId]
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>
