# 🚀 Vercel Deployment Rehberi

## ⚠️ Önemli Notlar

Frontend'inizde **dropdown ve ürünlerin görünmemesi** sorunu, backend API bağlantısından kaynaklanıyor. Vercel'de doğru çalışması için aşağıdaki adımları takip edin:

## 1. Backend'i Deploy Edin (Render.com)

Backend'iniz zaten Render'da: `https://mavus-backend.onrender.com`

### Backend CORS Ayarları ✅

Backend'de Vercel domain'i CORS'a eklendi:
- `https://mavus-g6p22.vercel.app`

## 2. Vercel Environment Variables

Vercel projenizde **Environment Variables** bölümüne gidin ve ekleyin:

```
VITE_API_URL=https://mavus-backend.onrender.com/api
```

### Nasıl Eklenir:

1. Vercel Dashboard → Projeniz → Settings
2. Environment Variables sekmesine gidin
3. Name: `VITE_API_URL`
4. Value: `https://mavus-backend.onrender.com/api`
5. Environment: **Production**, **Preview**, **Development** (hepsini seçin)
6. **Save** butonuna tıklayın

## 3. Yeniden Deploy Edin

Environment variable ekledikten sonra:

1. Vercel Dashboard → Deployments
2. En son deployment'ın yanındaki "..." → **Redeploy**
3. "Use existing Build Cache" seçeneğini **KAPATIN** (önemli!)
4. Redeploy'a tıklayın

## 4. Backend'de Django Settings

Backend'in `.env` dosyasında (Render.com'da):

```env
CORS_ALLOWED_ORIGINS=http://localhost:5173,http://127.0.0.1:5173,http://localhost:5176,http://127.0.0.1:5176,http://localhost:3000,https://mavus-g6p22.vercel.app

ALLOWED_HOSTS=localhost,127.0.0.1,mavus-backend.onrender.com
```

## 5. Test Edin

Deploy tamamlandıktan sonra:

1. `https://mavus-g6p22.vercel.app` adresini açın
2. Browser console'u açın (F12)
3. Network tab'ına bakın
4. API isteklerinin `https://mavus-backend.onrender.com/api/` adresine gittiğini kontrol edin

## 🐛 Sorun Giderme

### Dropdown Görünmüyor:
- **Sebep:** API'den kategoriler gelmiyor
- **Çözüm:** Environment variable'ı kontrol edin ve redeploy yapın

### Ürünler Görünmüyor:
- **Sebep:** API'den ürünler gelmiyor
- **Çözüm:**
  1. Backend'in çalıştığını kontrol edin: `https://mavus-backend.onrender.com/api/products/`
  2. CORS hatası varsa backend settings'i kontrol edin

### API Hatası (CORS):
- **Sebep:** Backend CORS ayarları yanlış
- **Çözüm:**
  1. Render.com'da Environment Variables'a gidin
  2. `CORS_ALLOWED_ORIGINS` değerine Vercel URL'inizi ekleyin
  3. Backend'i yeniden başlatın

## 📝 Build Komutu (Gerekirse)

Lokal olarak build almak için:

```bash
cd frontend
npm run build
```

Build çıktısı `frontend/dist/` klasörüne gelir.

## ✅ Deployment Checklist

- [x] Backend CORS ayarlarına Vercel URL eklendi
- [x] Frontend `.env` dosyası oluşturuldu
- [ ] Vercel'de Environment Variable eklendi
- [ ] Vercel'de redeploy yapıldı (cache kullanılmadan)
- [ ] Site test edildi

## 🎯 Son Notlar

- Backend free tier kullanıyorsanız ilk istek yavaş olabilir (cold start)
- Environment variable değişikliklerinden sonra mutlaka **cache kullanmadan** redeploy yapın
- Browser cache'ini temizleyin (Ctrl+Shift+R)

---

💡 **İpucu:** Eğer hala sorun yaşıyorsanız, Vercel deployment log'larını kontrol edin.
