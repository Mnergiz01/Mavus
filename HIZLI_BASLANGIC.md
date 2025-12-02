# ⚡ HIZLI BAŞLANGIÇ - Production Güncelleme

## 🎯 Sorun Ne?

Vercel'deki sitenizde dropdown ve ürünler görünmüyor çünkü **production database'de eski veriler var**.

## ✅ Çözüm (2 Dakika)

### 1️⃣ Render'da Deploy Et

1. [Render Dashboard](https://dashboard.render.com/) → Backend servisiniz
2. **Manual Deploy** → **Deploy latest commit**
3. Bekle (1-2 dakika)

### 2️⃣ Admin Panel'den Güncelle

1. [Admin Panel'e Git](https://mavus-backend.onrender.com/admin/)
2. Kullanıcı adı ve şifrenle giriş yap
3. **Categories** → Herhangi birini seç (checkbox)
4. Action: **"🚀 Update Production Database"** → Go
5. Onay ver

### 3️⃣ Test Et

[Vercel Sitesini Aç](https://mavus-g6p22.vercel.app)

Navbar'da kategoriler üzerine gel → Dropdown'da 5 kategori görünmeli:
- ✅ Yüzük
- ✅ Kolye
- ✅ Bileklik
- ✅ Küpe
- ✅ Set

---

## 📖 Detaylı Bilgi

Daha fazla bilgi için: [PRODUCTION_UPDATE_NO_SHELL.md](PRODUCTION_UPDATE_NO_SHELL.md)

---

## 🆘 Sorun mu var?

**Admin'de action görünmüyor:**
- Adım 1'i tekrar yap (Render'da deploy)

**Vercel hala eski:**
- Browser cache temizle: Ctrl+Shift+R
- API'yi test et: https://mavus-backend.onrender.com/api/categories/

**Başka sorun:**
- [Detaylı Rehber](PRODUCTION_UPDATE_NO_SHELL.md)
