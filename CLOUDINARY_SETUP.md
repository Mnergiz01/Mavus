# Cloudinary Kurulum Rehberi

Production ortamında (Render) resim yükleme özelliğinin çalışması için Cloudinary hesabı gereklidir.

## Adımlar:

### 1. Cloudinary Hesabı Oluşturun
- https://cloudinary.com adresine gidin
- Ücretsiz hesap oluşturun

### 2. API Bilgilerinizi Alın
- Dashboard'a gidin
- Şu bilgileri bulun:
  - Cloud Name
  - API Key
  - API Secret

### 3. Render'da Environment Variables Ekleyin
Render Dashboard → Backend Service → Environment → Add Environment Variables:

```
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

### 4. Render'ı Yeniden Deploy Edin
- Değişiklikleri kaydedin
- Render otomatik olarak yeniden deploy edecek

## Local Geliştirme

Local'de dosya yükleme varsayılan olarak `media/` klasörüne kaydedilir.
Cloudinary kullanmak isterseniz `.env` dosyasına şu satırları ekleyin:

```
DEBUG=False
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

## Kullanım

Admin panelinden artık hem URL hem de dosya yükleyebilirsiniz:
- URL: Harici bir resim linki
- Dosya: Bilgisayarınızdan dosya yükleme

**Not:** Dosya yükleme önceliklidir. Hem URL hem dosya varsa, dosya kullanılır.
