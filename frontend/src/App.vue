<script setup>
import { onMounted, onUnmounted } from 'vue'
import Navbar from './components/Navbar.vue'
import Footer from './components/Footer.vue'
import { useProducts } from './composables/useProducts'
import { useExchangeRates } from './composables/useExchangeRates'

const { fetchProducts, fetchCategories } = useProducts()
const { fetchExchangeRates } = useExchangeRates()

let exchangeRateInterval = null

onMounted(() => {
  fetchProducts()
  fetchCategories()
  fetchExchangeRates()

  // Update exchange rates every 5 minutes
  exchangeRateInterval = setInterval(() => {
    fetchExchangeRates()
  }, 5 * 60 * 1000)
})

onUnmounted(() => {
  clearInterval(exchangeRateInterval)
})
</script>

<template>
  <div class="min-h-screen bg-white">
    <Navbar />
    <router-view />
    <Footer />
  </div>
</template>

<style scoped>
/* Animations */
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

@keyframes fade-in-up {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes slide-in-left {
  from {
    opacity: 0;
    transform: translateX(-30px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes slide-in-right {
  from {
    opacity: 0;
    transform: translateX(30px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes scale-in {
  from {
    opacity: 0;
    transform: scale(0.9);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

.animate-fade-in {
  animation: fade-in 0.6s ease-out;
}

.animate-fade-in-up {
  animation: fade-in-up 0.8s ease-out;
}

.animate-slide-in-left {
  animation: slide-in-left 0.6s ease-out;
}

.animate-slide-in-right {
  animation: slide-in-right 0.6s ease-out;
}

.animate-scale-in {
  animation: scale-in 0.5s ease-out;
}

/* Hide scrollbar but keep functionality */
.scrollbar-hide {
  -ms-overflow-style: none;
  scrollbar-width: none;
}

.scrollbar-hide::-webkit-scrollbar {
  display: none;
}
</style>
