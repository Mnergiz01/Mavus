# Render External Database URL ile Setup

## 🔑 External Database URL'ini Alın

1. https://dashboard.render.com → PostgreSQL → mavus-db
2. **"External Database URL"** kopyalayın (Internal değil!)
3. Şuna benzer olacak:
   ```
   postgresql://mavus_user:XXXX@dpg-xxxx.oregon-postgres.render.com/mavus_production
   ```

## 🚀 Script'i Çalıştırın

```bash
cd /Users/muzaffernergiz/Desktop/Projelerim/Mavus
source venv/bin/activate
python remote_setup.py
```

**External Database URL**'ini yapıştırın!

---

## ⚠️ Önemli Not

- ❌ **Internal Database URL** → Local'den çalışmaz
- ✅ **External Database URL** → Local'den çalışır

External URL'de `.render.com` domain'i olmalı!
