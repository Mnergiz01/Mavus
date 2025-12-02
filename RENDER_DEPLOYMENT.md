# Mavus Projesini Render.com'a Deploy Etme Rehberi

Bu rehber, Django + Vue.js projenizi Render.com'da ücretsiz olarak canlıya almanız için adım adım talimatlar içerir.

## 📋 Gereksinimler

- GitHub hesabı
- Render.com hesabı (ücretsiz)
- Git yüklü olmalı

---

## 🚀 ADIM 1: GitHub'a Projeyi Yükleyin

### 1.1 Git Repository Oluşturun (Eğer yoksa)

```bash
cd /Users/muzaffernergiz/Desktop/Projelerim/Mavus

# Git initialize
git init

# .gitignore kontrolü (varsa zaten)
cat .gitignore

# Tüm dosyaları ekle
git add .

# İlk commit
git commit -m "Initial commit for Render deployment"
```

### 1.2 GitHub'da Repository Oluşturun

1. https://github.com adresine gidin
2. Sağ üstteki "+" butonuna tıklayın → "New repository"
3. Repository adı: `Mavus` (veya istediğiniz isim)
4. Public veya Private seçin
5. **"Add a README file" seçeneğini SEÇMEYİN** (zaten dosyalarınız var)
6. "Create repository" tıklayın

### 1.3 GitHub'a Push Edin

GitHub'da oluşturduğunuz repository sayfasında gösterilen komutları çalıştırın:

```bash
git remote add origin https://github.com/KULLANICI_ADINIZ/Mavus.git
git branch -M main
git push -u origin main
```

---

## 🌐 ADIM 2: Render.com'da Backend (Django) Kurulumu

### 2.1 Render'a Kaydolun

1. https://render.com adresine gidin
2. "Get Started for Free" tıklayın
3. GitHub hesabınızla giriş yapın

### 2.2 PostgreSQL Database Oluşturun

1. Dashboard'da **"New +"** → **"PostgreSQL"** seçin
2. Ayarlar:
   - **Name:** `mavus-db`
   - **Database:** `mavus_production`
   - **User:** `mavus_user`
   - **Region:** Frankfurt (veya size yakın)
   - **Plan:** Free
3. **"Create Database"** tıklayın
4. ⏳ Database oluşturulmasını bekleyin (1-2 dakika)
5. ✅ Database oluşturulduktan sonra **Internal Database URL**'i kopyalayın

### 2.3 Web Service (Django Backend) Oluşturun

1. Dashboard'da **"New +"** → **"Web Service"** seçin
2. GitHub repository'nizi seçin: `Mavus`
3. Ayarlar:
   - **Name:** `mavus-backend`
   - **Region:** Frankfurt
   - **Branch:** `main`
   - **Root Directory:** (boş bırakın)
   - **Runtime:** `Python 3`
   - **Build Command:** `./build.sh`
   - **Start Command:** `gunicorn mavus_project.wsgi:application`
   - **Plan:** Free

4. **Environment Variables** (Ortam Değişkenleri) ekleyin:

   **"Add Environment Variable"** butonuna tıklayarak aşağıdaki değişkenleri ekleyin:

   | Key | Value |
   |-----|-------|
   | `PYTHON_VERSION` | `3.12.0` |
   | `SECRET_KEY` | (Generate ile otomatik oluştur) |
   | `DEBUG` | `False` |
   | `DATABASE_URL` | (PostgreSQL'den kopyaladığınız Internal Database URL) |
   | `ALLOWED_HOSTS` | `mavus-backend.onrender.com` (veya size verilen URL) |
   | `CORS_ALLOWED_ORIGINS` | `https://mavus-frontend.onrender.com` (frontend URL'inizi buraya yazacaksınız) |

5. **"Create Web Service"** tıklayın
6. ⏳ Deploy işlemini bekleyin (5-10 dakika)

### 2.4 Deploy Loglarını Kontrol Edin

- Dashboard'da servisinize tıklayın
- "Logs" sekmesinden deploy durumunu izleyin
- ✅ "Your service is live" mesajını görünce hazır!

### 2.5 Admin Kullanıcısı Oluşturun

Deploy tamamlandıktan sonra:

1. Servis sayfasında **"Shell"** sekmesine gidin
2. Aşağıdaki komutu çalıştırın:

```bash
python manage.py createsuperuser
```

3. Kullanıcı adı, email ve şifre girin

---

## 🎨 ADIM 3: Frontend (Vue.js) Kurulumu

### Seçenek A: Vercel (Önerilen - Daha Kolay)

1. https://vercel.com adresine gidin
2. GitHub ile giriş yapın
3. "Add New Project" → Repository'nizi seçin
4. Ayarlar:
   - **Root Directory:** `frontend`
   - **Framework Preset:** Vite
   - **Build Command:** `npm run build`
   - **Output Directory:** `dist`
5. **Environment Variables** ekleyin:
   - `VITE_API_URL` → `https://mavus-backend.onrender.com/api`
6. "Deploy" tıklayın

### Seçenek B: Render Static Site

1. Dashboard'da **"New +"** → **"Static Site"** seçin
2. Repository'nizi seçin
3. Ayarlar:
   - **Name:** `mavus-frontend`
   - **Root Directory:** `frontend`
   - **Build Command:** `npm run build`
   - **Publish Directory:** `frontend/dist`
4. **Environment Variables:**
   - `VITE_API_URL` → `https://mavus-backend.onrender.com/api`
5. "Create Static Site" tıklayın

---

## 🔧 ADIM 4: Final Ayarlar

### 4.1 Backend Environment Variables'ı Güncelleyin

1. Backend servisinize gidin → "Environment" sekmesi
2. `CORS_ALLOWED_ORIGINS` değerini frontend URL'iniz ile güncelleyin:
   ```
   https://mavus-frontend.vercel.app
   ```
3. `ALLOWED_HOSTS` değerini güncelleyin:
   ```
   mavus-backend.onrender.com,mavus-frontend.vercel.app
   ```
4. **"Save Changes"** ve otomatik re-deploy bekleyin

### 4.2 Frontend API URL'ini Güncelleyin

Eğer `.env.production` dosyasını kullanıyorsanız:

```env
VITE_API_URL=https://mavus-backend.onrender.com/api
```

Değişiklik yaptıysanız, commit edip push edin:

```bash
git add .
git commit -m "Update API URL for production"
git push
```

---

## ✅ Test Edin!

### Backend Test:
```
https://mavus-backend.onrender.com/api/products/
https://mavus-backend.onrender.com/api/categories/
https://mavus-backend.onrender.com/admin/
```

### Frontend Test:
```
https://mavus-frontend.vercel.app
```

---

## 📊 Ücretsiz Plan Limitleri

### Render Free Tier:
- ✅ 750 saat/ay (yeterli)
- ✅ 512 MB RAM
- ✅ PostgreSQL 1GB storage
- ⚠️ 15 dakika kullanılmazsa uyku moduna geçer (ilk istek 30 saniye sürebilir)

### Vercel Free Tier:
- ✅ Sınırsız deployment
- ✅ 100 GB bandwidth/ay
- ✅ Otomatik SSL sertifikası

---

## 🔄 Güncelleme Nasıl Yapılır?

Kod değişikliği yaptığınızda:

```bash
git add .
git commit -m "Yaptığınız değişiklik açıklaması"
git push
```

Render ve Vercel otomatik olarak yeni kodu deploy edecektir!

---

## 🐛 Sorun Giderme

### Backend 503 Hatası
- Render free tier 15 dakika sonra uyur
- İlk istekte 30 saniye bekleyin

### Static Files Görünmüyor
```bash
# Render shell'de
python manage.py collectstatic --no-input
```

### Database Connection Error
- `DATABASE_URL` doğru kopyalandığını kontrol edin
- Internal Database URL kullandığınızdan emin olun

### CORS Hatası
- `CORS_ALLOWED_ORIGINS` frontend URL'inizi içermeli
- Protokol kontrolü: `https://` ile başlamalı

---

## 📞 Yararlı Linkler

- Render Docs: https://render.com/docs
- Vercel Docs: https://vercel.com/docs
- Django Deployment: https://docs.djangoproject.com/en/stable/howto/deployment/

---

## 🎉 Tebrikler!

Projeniz artık canlıda! 🚀

**Backend URL:** https://mavus-backend.onrender.com
**Frontend URL:** https://mavus-frontend.vercel.app
**Admin Panel:** https://mavus-backend.onrender.com/admin/
