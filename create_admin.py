#!/usr/bin/env python
"""
Render'da admin kullanıcısı oluşturmak için tek satırlık script
Bu dosyayı Render'ın one-off job olarak çalıştırabilirsiniz
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mavus_project.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@mavus.com', 'admin123')
    print('✅ Admin created: username=admin, password=admin123')
else:
    print('ℹ️  Admin already exists')
