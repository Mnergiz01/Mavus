<template>
  <div class="min-h-screen pt-24 pb-20 bg-gradient-to-b from-white via-amber-50/20 to-white">
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

      <!-- Hero Section -->
      <div class="max-w-7xl mx-auto mb-20">
        <div class="text-center mb-16 animate-fade-in">
          <div class="inline-block mb-6">
            <div class="relative">
              <div class="absolute inset-0 bg-amber-400 blur-3xl opacity-30 animate-pulse"></div>
              <SparklesIcon class="h-20 w-20 text-amber-500 relative z-10 mx-auto" />
            </div>
          </div>
          <h1 class="text-5xl md:text-6xl font-serif font-bold text-slate-900 mb-6 animate-slide-in-right">
            Hakkımızda
          </h1>
          <div class="w-24 h-1.5 bg-gradient-to-r from-amber-500 to-amber-600 mx-auto rounded-full mb-8"></div>
          <p class="text-xl text-slate-600 max-w-3xl mx-auto leading-relaxed">
            1975 yılından bu yana Kahramanmaraş'ın güvenilir kuyumcusu
          </p>
        </div>

        <!-- Story Section with Image -->
        <div class="grid lg:grid-cols-2 gap-12 items-center mb-20">
          <!-- Image -->
          <div class="relative group animate-slide-in-left">
            <div class="absolute -inset-4 bg-gradient-to-r from-amber-400 to-amber-600 rounded-3xl opacity-20 group-hover:opacity-30 transition-opacity blur-xl"></div>
            <div class="relative aspect-[4/3] rounded-3xl overflow-hidden shadow-2xl">
              <img
                src="https://images.unsplash.com/photo-1611591437281-460bfbe1220a?w=800&h=600&fit=crop"
                alt="Mawuş Kuyumculuk Mağaza"
                class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700"
              />
              <div class="absolute inset-0 bg-gradient-to-t from-slate-900/50 to-transparent"></div>
            </div>
          </div>

          <!-- Content -->
          <div class="space-y-6 animate-slide-in-right">
            <h2 class="text-4xl font-serif font-bold text-slate-900 mb-4">
              Hikayemiz
            </h2>
            <p class="text-lg text-slate-600 leading-relaxed">
              1975 yılında Kahramanmaraş'ın kalbinde açtığımız küçük bir atölyeden, bugünün modern ve güvenilir kuyumculuk markasına uzanan yolculuğumuz, tutkuyla örülmüş bir hikaye.
            </p>
            <p class="text-lg text-slate-600 leading-relaxed">
              50 yıla yakın tecrübemiz ile, geleneksel el işçiliğini modern tasarım anlayışıyla birleştirerek, her biri özenle hazırlanmış eşsiz parçalar üretiyoruz.
            </p>
            <p class="text-lg text-slate-600 leading-relaxed">
              Mawuş Kuyumculuk olarak, her müşterimize özel anlarında eşlik edebilmek, hayallerindeki mücevheri sunabilmek bizim için en büyük mutluluk kaynağı.
            </p>
          </div>
        </div>

        <!-- Values Section -->
        <div class="mb-20">
          <h2 class="text-4xl font-serif font-bold text-slate-900 text-center mb-12 animate-fade-in">
            Değerlerimiz
          </h2>
          <div class="grid md:grid-cols-3 gap-8">
            <!-- Value 1 -->
            <div class="bg-white p-8 rounded-2xl shadow-xl hover:shadow-2xl transition-all duration-500 transform hover:-translate-y-2 animate-scale-in border border-amber-100">
              <div class="w-16 h-16 bg-gradient-to-br from-amber-500 to-amber-600 rounded-2xl flex items-center justify-center mb-6 mx-auto">
                <ShieldCheckIcon class="h-8 w-8 text-white" />
              </div>
              <h3 class="text-2xl font-bold text-slate-900 mb-4 text-center">Güven</h3>
              <p class="text-slate-600 text-center leading-relaxed">
                50 yıllık tecrübemiz ve sayısız mutlu müşterimizle, güvenin adresi olduk.
              </p>
            </div>

            <!-- Value 2 -->
            <div class="bg-white p-8 rounded-2xl shadow-xl hover:shadow-2xl transition-all duration-500 transform hover:-translate-y-2 animate-scale-in border border-amber-100" style="animation-delay: 0.1s">
              <div class="w-16 h-16 bg-gradient-to-br from-amber-500 to-amber-600 rounded-2xl flex items-center justify-center mb-6 mx-auto">
                <StarIcon class="h-8 w-8 text-white" />
              </div>
              <h3 class="text-2xl font-bold text-slate-900 mb-4 text-center">Kalite</h3>
              <p class="text-slate-600 text-center leading-relaxed">
                En kaliteli hammadde ve ustaca işçilikle, her parçayı sanat eserine dönüştürüyoruz.
              </p>
            </div>

            <!-- Value 3 -->
            <div class="bg-white p-8 rounded-2xl shadow-xl hover:shadow-2xl transition-all duration-500 transform hover:-translate-y-2 animate-scale-in border border-amber-100" style="animation-delay: 0.2s">
              <div class="w-16 h-16 bg-gradient-to-br from-amber-500 to-amber-600 rounded-2xl flex items-center justify-center mb-6 mx-auto">
                <SparklesIcon class="h-8 w-8 text-white" />
              </div>
              <h3 class="text-2xl font-bold text-slate-900 mb-4 text-center">Benzersizlik</h3>
              <p class="text-slate-600 text-center leading-relaxed">
                Her tasarım özgün, her parça özel. Sizi yansıtan mücevherler yaratıyoruz.
              </p>
            </div>
          </div>
        </div>

        <!-- Contact CTA -->
        <div class="bg-gradient-to-r from-amber-600 via-amber-500 to-amber-600 rounded-3xl p-12 text-center text-white animate-fade-in shadow-2xl">
          <h2 class="text-4xl font-serif font-bold mb-4">Bizi Ziyaret Edin</h2>
          <p class="text-lg mb-8 opacity-90">Mağazamızda sizi ağırlamaktan mutluluk duyarız</p>
          <div class="flex flex-col md:flex-row items-center justify-center gap-6">
            <a
              href="https://www.google.com/maps/place/Mawu%C5%9F+Kuyumculuk/@37.5926992,36.8617765,17z/data=!3m1!4b1!4m6!3m5!1s0x152ddb52e9cdc5b7:0xa19f28423279ebca!8m2!3d37.592695!4d36.8643514!16s%2Fg%2F11m5hkbkly?entry=ttu&g_ep=EgoyMDI1MTEyMy4xIKXMDSoASAFQAw%3D%3D"
              target="_blank"
              class="px-8 py-4 bg-white text-amber-600 rounded-xl font-bold hover:bg-amber-50 transition-all duration-300 shadow-xl hover:shadow-2xl transform hover:scale-105"
            >
              Haritada Görüntüle
            </a>
            <a
              href="https://wa.me/905452409490"
              target="_blank"
              class="px-8 py-4 bg-green-600 text-white rounded-xl font-bold hover:bg-green-700 transition-all duration-300 shadow-xl hover:shadow-2xl transform hover:scale-105"
            >
              WhatsApp ile İletişime Geç
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { SparklesIcon, ShieldCheckIcon, StarIcon } from '@heroicons/vue/24/outline'
</script>
