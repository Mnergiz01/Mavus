# ⚡ Hızlı Çözüm - Vercel Dropdown ve Ürünler Görünmüyor

## 🎯 Ana Sorun

Vercel'deki sitenizde dropdown ve ürünler görünmüyor çünkü **API bağlantısı kurulamıyor**.

## ✅ Çözüm (3 Adım)

### 1️⃣ Vercel Environment Variable Ekle

1. [Vercel Dashboard](https://vercel.com/dashboard) → Projeniz
2. **Settings** → **Environment Variables**
3. Yeni ekle:
   - **Name:** `VITE_API_URL`
   - **Value:** `https://mavus-backend.onrender.com/api`
   - **Environments:** Production, Preview, Development (HEPSİNİ seç!)
4. **Save**

### 2️⃣ Redeploy (ÖNEMLİ!)

1. **Deployments** sekmesine git
2. En son deployment'ı bul
3. **"..."** → **Redeploy**
4. **"Use existing Build Cache"** seçeneğini **KAPATIN** ✗
5. **Redeploy** butonuna bas

### 3️⃣ Test Et

1. `https://mavus-g6p22.vercel.app` adresini aç
2. F12 → Console → Network
3. `/api/categories/` ve `/api/products/` isteklerini kontrol et

## 🔍 Hala Çalışmıyor mu?

### Backend Kontrol:
Bu link açılıyor mu? → https://mavus-backend.onrender.com/api/products/

- ✅ **Açılıyorsa:** Vercel environment variable yanlış, tekrar kontrol et
- ❌ **Açılmıyorsa:** Backend çökmüş, Render.com'da restart et

### CORS Hatası:
Console'da CORS hatası varsa → Backend'in `.env` dosyasına Vercel URL'ini ekle:

```
CORS_ALLOWED_ORIGINS=https://mavus-g6p22.vercel.app
```

## 💡 Önemli Notlar

- Environment variable ekledikten sonra **mutlaka cache KULLANMADAN redeploy et**
- Backend free tier ise ilk istek 30 saniye sürebilir
- Browser cache'i temizle (Ctrl+Shift+R)

---

**Hala sorun varsa console log'larını kontrol et!**
