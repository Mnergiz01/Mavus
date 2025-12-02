# Mavus Projesi Canlıya Alma Rehberi

Bu rehber, Mavus Django + Vue.js projenizi bir sunucuda canlıya almanız için gereken tüm adımları içermektedir.

## 📋 İçindekiler
1. [Gereksinimler](#gereksinimler)
2. [Domain ve Hosting Satın Alma](#domain-ve-hosting-satın-alma)
3. [Sunucu Kurulumu](#sunucu-kurulumu)
4. [Otomatik Kurulum](#otomatik-kurulum)
5. [Manuel Kurulum](#manuel-kurulum)
6. [SSL Sertifikası Kurulumu](#ssl-sertifikası-kurulumu)
7. [Güncelleme ve Bakım](#güncelleme-ve-bakım)

---

## 🔧 Gereksinimler

### Sunucu Gereksinimleri
- **İşletim Sistemi:** Ubuntu 20.04+ veya Debian 11+
- **RAM:** Minimum 2GB (4GB önerilir)
- **CPU:** Minimum 1 vCPU (2 vCPU önerilir)
- **Disk:** Minimum 20GB SSD
- **Python:** 3.8+
- **Node.js:** 18+
- **PostgreSQL:** 14+

---

## 🌐 Domain ve Hosting Satın Alma

### Adım 1: Domain Satın Alma

#### Türk Sağlayıcılar
1. **Natro.com**
   - https://www.natro.com adresine gidin
   - Domain arama bölümünden istediğiniz ismi arayın
   - `.com.tr` veya `.com` seçeneklerini değerlendirin
   - Fiyat: ~50-150 TL/yıl

2. **Turhost.com**
   - https://www.turhost.com
   - Benzer süreç
   - Fiyat: ~60-180 TL/yıl

3. **Hostinger**
   - https://www.hostinger.com.tr
   - Uluslararası, Türkçe destek
   - Fiyat: ~$8-15/yıl

#### Uluslararası Sağlayıcılar
1. **Namecheap** - https://www.namecheap.com (~$10/yıl)
2. **GoDaddy** - https://www.godaddy.com (~$12/yıl)
3. **Google Domains** - https://domains.google (~$12/yıl)

### Adım 2: Hosting/VPS Seçimi

#### Seçenek A: VPS/Cloud Hosting (Önerilen - Tam Kontrol)

**Neden VPS?**
- Django + PostgreSQL için tam kontrol
- Daha güvenli ve performanslı
- Kendi sunucu ayarlarınızı yapabilirsiniz

**Önerilen Sağlayıcılar:**

1. **DigitalOcean** (Önerilen)
   - Site: https://www.digitalocean.com
   - Paket: Basic Droplet - $12/ay (2GB RAM)
   - Özellikler: Ubuntu 22.04, kolay kurulum, iyi dokümantasyon
   - Kredi kartı gerekli

2. **Hetzner** (Ekonomik)
   - Site: https://www.hetzner.com
   - Paket: CX21 - €5.83/ay (2GB RAM)
   - Özellikler: Avrupa lokasyonu, uygun fiyat

3. **Linode/Akamai**
   - Site: https://www.linode.com
   - Paket: Nanode 2GB - $12/ay
   - Özellikler: Güvenilir, iyi performans

4. **AWS Lightsail**
   - Site: https://aws.amazon.com/lightsail
   - Paket: $5-10/ay
   - Özellikler: AWS altyapısı, güvenilir

5. **Türk Alternatifler**
   - **Turhost VDS:** https://www.turhost.com/vds - 200-400 TL/ay
   - **Natro Cloud:** https://www.natro.com - 150-350 TL/ay

#### Seçenek B: Paylaşımlı Hosting (Başlangıç için)
**Not:** Django desteği olan paylaşımlı hosting bulmak zor. VPS önerilir.

#### Seçenek C: Ücretsiz/Test Platformları
Proje test etmek için:
1. **Railway.app** - Backend için ücretsiz tier
2. **Render.com** - Backend için ücretsiz tier (yavaş başlatma)
3. **Vercel/Netlify** - Frontend için

---

## 🚀 Sunucu Kurulumu

### Adım 3: VPS Satın Alma ve Kurulum (DigitalOcean Örneği)

1. **DigitalOcean'a kayıt olun**
   ```
   https://www.digitalocean.com/try/free-trial
   İlk kayıtta $200 kredi (60 gün geçerli)
   ```

2. **Droplet oluşturun**
   - "Create" > "Droplets" tıklayın
   - **Image:** Ubuntu 22.04 LTS
   - **Plan:** Basic - $12/ay (2GB RAM, 1 vCPU, 50GB SSD)
   - **Datacenter:** Frankfurt veya Amsterdam (Türkiye'ye yakın)
   - **Authentication:** SSH Key (önerilir) veya Password
   - **Hostname:** mavus-production
   - "Create Droplet" tıklayın

3. **Sunucu IP adresinizi not alın**
   - Droplet oluşturulduktan sonra IP adresini kopyalayın
   - Örnek: `157.230.123.456`

### Adım 4: Domain'i Sunucuya Yönlendirme

1. **Domain sağlayıcınızın DNS yönetim paneline gidin**

2. **A kayıtları ekleyin:**
   ```
   Type: A
   Host: @
   Value: [Sunucu-IP-Adresi]
   TTL: 3600

   Type: A
   Host: www
   Value: [Sunucu-IP-Adresi]
   TTL: 3600
   ```

3. **DNS yayılmasını bekleyin (5-30 dakika)**

### Adım 5: Sunucuya Bağlanma

```bash
# SSH ile bağlanın
ssh root@[sunucu-ip-adresi]

# İlk giriş için şifrenizi girin (email ile gönderilmiş)
```

---

## ⚡ Otomatik Kurulum

### Hızlı Kurulum (Önerilen)

1. **Setup script'ini sunucuya kopyalayın**
```bash
# Yerel makinenizden
scp setup_server.sh root@[sunucu-ip]:/root/
```

2. **Sunucuda çalıştırın**
```bash
# Sunucuda
chmod +x /root/setup_server.sh
sudo /root/setup_server.sh
```

3. **Script sizden şunları soracak:**
   - Database adı (varsayılan: mavus_production)
   - Database kullanıcısı (varsayılan: mavus_user)
   - Database şifresi
   - Git repository URL

4. **Kurulum tamamlandıktan sonra:**
```bash
# Domain adını güncelleyin
sudo nano /var/www/mavus/.env
# ALLOWED_HOSTS ve CORS_ALLOWED_ORIGINS değerlerini güncelleyin

# NGINX config'i güncelleyin
sudo nano /etc/nginx/sites-available/mavus
# yourdomain.com yazan yerleri kendi domain'iniz ile değiştirin

# Servisleri yeniden başlatın
sudo systemctl restart gunicorn
sudo systemctl restart nginx

# SSL sertifikası kurun
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com

# Django admin kullanıcısı oluşturun
cd /var/www/mavus
source venv/bin/activate
python manage.py createsuperuser
```

---

## 🔨 Manuel Kurulum

### Adım 1: Sistem Paketlerini Güncelleme

```bash
sudo apt update && sudo apt upgrade -y
```

### Adım 2: Gerekli Paketleri Kurma

```bash
# Python ve ilgili araçlar
sudo apt install -y python3 python3-pip python3-venv

# PostgreSQL
sudo apt install -y postgresql postgresql-contrib

# NGINX
sudo apt install -y nginx

# Git ve diğer araçlar
sudo apt install -y git curl

# Node.js ve npm
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs
```

### Adım 3: PostgreSQL Veritabanı Oluşturma

```bash
sudo -u postgres psql

# PostgreSQL içinde:
CREATE DATABASE mavus_production;
CREATE USER mavus_user WITH PASSWORD 'güçlü_şifre_buraya';
ALTER ROLE mavus_user SET client_encoding TO 'utf8';
ALTER ROLE mavus_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE mavus_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE mavus_production TO mavus_user;
\q
```

### Adım 4: Proje Dizini Oluşturma

```bash
sudo mkdir -p /var/www/mavus
sudo mkdir -p /var/log/gunicorn
sudo mkdir -p /var/run/gunicorn
cd /var/www/mavus
```

### Adım 5: Projeyi Sunucuya Yükleme

**Seçenek A: Git ile (Önerilen)**
```bash
cd /var/www/mavus
git clone [git-repository-url] .
```

**Seçenek B: SCP ile yerel makineden kopyalama**
```bash
# Yerel makinenizde (Mac/Linux terminal):
cd /Users/muzaffernergiz/Desktop/Projelerim/Mavus
scp -r * root@[sunucu-ip]:/var/www/mavus/
```

### Adım 6: Python Virtual Environment Kurulumu

```bash
cd /var/www/mavus
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### Adım 7: .env Dosyası Oluşturma

```bash
cd /var/www/mavus
nano .env
```

İçeriği `.env.example` dosyasından kopyalayıp değerleri doldurun:
```env
SECRET_KEY=buraya_güçlü_bir_key_üretin
DEBUG=False
DB_NAME=mavus_production
DB_USER=mavus_user
DB_PASSWORD=veritabanı_şifreniz
DB_HOST=localhost
DB_PORT=5432
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com,sunucu_ip
CORS_ALLOWED_ORIGINS=https://yourdomain.com,https://www.yourdomain.com
```

**Secret key üretmek için:**
```bash
python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

### Adım 8: Django Migrations ve Static Files

```bash
cd /var/www/mavus
source venv/bin/activate
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
```

### Adım 9: Frontend Build

```bash
cd /var/www/mavus/frontend
npm install
npm run build
```

### Adım 10: Gunicorn Servisini Kurma

```bash
# Gunicorn config dosyasını kontrol edin
cat /var/www/mavus/gunicorn_config.py

# Systemd servis dosyasını kopyalayın
sudo cp /var/www/mavus/systemd_gunicorn.service /etc/systemd/system/gunicorn.service

# Servisi başlatın
sudo systemctl daemon-reload
sudo systemctl enable gunicorn
sudo systemctl start gunicorn
sudo systemctl status gunicorn
```

### Adım 11: NGINX Kurulumu

```bash
# NGINX config dosyasını kopyalayın
sudo cp /var/www/mavus/nginx.conf /etc/nginx/sites-available/mavus

# Config'i düzenleyin - domain adını değiştirin
sudo nano /etc/nginx/sites-available/mavus
# yourdomain.com yazan tüm yerleri kendi domain'iniz ile değiştirin

# Symlink oluşturun
sudo ln -s /etc/nginx/sites-available/mavus /etc/nginx/sites-enabled/

# Varsayılan siteyi devre dışı bırakın
sudo rm /etc/nginx/sites-enabled/default

# Config'i test edin
sudo nginx -t

# NGINX'i başlatın
sudo systemctl restart nginx
```

### Adım 12: İzinleri Ayarlama

```bash
sudo chown -R www-data:www-data /var/www/mavus
sudo chmod +x /var/www/mavus/deploy.sh
```

---

## 🔒 SSL Sertifikası Kurulumu

Let's Encrypt ile ücretsiz SSL sertifikası:

```bash
# Certbot kurulumu
sudo apt install -y certbot python3-certbot-nginx

# SSL sertifikası al ve NGINX'e otomatik entegre et
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com

# Email adresinizi girin
# Terms of Service'i kabul edin
# HTTPS yönlendirmesini aktif edin (önerilen)
```

Sertifika otomatik olarak yenilenecektir. Test etmek için:
```bash
sudo certbot renew --dry-run
```

---

## 🔄 Güncelleme ve Bakım

### Kod Güncellemesi (Git ile)

```bash
cd /var/www/mavus
./deploy.sh
```

veya manuel:

```bash
cd /var/www/mavus
git pull origin main
source venv/bin/activate
pip install -r requirements.txt --upgrade
python manage.py migrate
python manage.py collectstatic --noinput
cd frontend
npm install
npm run build
sudo systemctl restart gunicorn
sudo systemctl restart nginx
```

### Logları İnceleme

```bash
# Gunicorn logları
sudo tail -f /var/log/gunicorn/error.log
sudo tail -f /var/log/gunicorn/access.log

# NGINX logları
sudo tail -f /var/log/nginx/mavus_error.log
sudo tail -f /var/log/nginx/mavus_access.log

# Gunicorn servis durumu
sudo systemctl status gunicorn

# NGINX durumu
sudo systemctl status nginx
```

### Database Backup

```bash
# Backup alma
sudo -u postgres pg_dump mavus_production > backup_$(date +%Y%m%d).sql

# Backup'ı geri yükleme
sudo -u postgres psql mavus_production < backup_20231202.sql
```

---

## 🐛 Sorun Giderme

### Gunicorn başlamıyor
```bash
sudo systemctl status gunicorn
sudo journalctl -u gunicorn -f
```

### NGINX hata veriyor
```bash
sudo nginx -t
sudo tail -f /var/log/nginx/error.log
```

### Static dosyalar yüklenmiyor
```bash
python manage.py collectstatic --noinput
sudo systemctl restart nginx
```

### 502 Bad Gateway hatası
```bash
# Gunicorn çalışıyor mu kontrol edin
sudo systemctl status gunicorn
sudo systemctl restart gunicorn
```

### Database bağlantı hatası
```bash
# PostgreSQL çalışıyor mu?
sudo systemctl status postgresql

# .env dosyasındaki bilgileri kontrol edin
cat /var/www/mavus/.env

# PostgreSQL'e manuel bağlanmayı deneyin
psql -h localhost -U mavus_user -d mavus_production
```

---

## 📞 Destek ve Kaynaklar

- Django Deployment Docs: https://docs.djangoproject.com/en/stable/howto/deployment/
- Gunicorn Docs: https://docs.gunicorn.org/
- NGINX Docs: https://nginx.org/en/docs/
- DigitalOcean Tutorials: https://www.digitalocean.com/community/tutorials

---

## ✅ Kontrol Listesi

- [ ] Domain satın alındı
- [ ] VPS/Hosting satın alındı
- [ ] Domain DNS ayarları yapıldı
- [ ] Sunucuya SSH ile bağlanıldı
- [ ] Sistem paketleri kuruldu
- [ ] PostgreSQL veritabanı oluşturuldu
- [ ] Proje dosyaları yüklendi
- [ ] .env dosyası yapılandırıldı
- [ ] Python bağımlılıkları kuruldu
- [ ] Django migrations çalıştırıldı
- [ ] Frontend build alındı
- [ ] Gunicorn servisi kuruldu
- [ ] NGINX yapılandırıldı
- [ ] SSL sertifikası kuruldu
- [ ] Django superuser oluşturuldu
- [ ] Site test edildi

---

**Başarılar! Sorularınız için GitHub Issues açabilir veya dokümantasyonu inceleyebilirsiniz.**
