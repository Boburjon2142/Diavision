# PythonAnywhere Deployment Guide

## 1. Virtualenv

```bash
mkvirtualenv --python=/usr/bin/python3.11 diabet-heal-ai
pip install -r /home/yourusername/diabet-AI/requirements.txt
```

## 2. Environment file

`.env.example` nusxasidan `.env` yarating:

```bash
cp /home/yourusername/diabet-AI/.env.example /home/yourusername/diabet-AI/.env
```

Quyidagilarni moslang:

- `SECRET_KEY`
- `DEBUG=False`
- `ALLOWED_HOSTS=yourusername.pythonanywhere.com`
- `CSRF_TRUSTED_ORIGINS=https://yourusername.pythonanywhere.com`
- `ENABLE_HTTPS_SECURITY=True`

## 3. Migrations va superuser

```bash
cd /home/yourusername/diabet-AI
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata sample_data.json
python manage.py createsuperuser
```

## 4. Static files

```bash
python manage.py collectstatic --noinput
```

PythonAnywhere Web tab’da:

- URL: `/static/`
- Directory: `/home/yourusername/diabet-AI/staticfiles`

## 5. WSGI configuration

Web tab’dagi WSGI faylni [diabet_heal_ai/pythonanywhere_wsgi.py](/c:/Users/Omen/Desktop/diabet-AI/diabet_heal_ai/pythonanywhere_wsgi.py) asosida moslang.

Muhim yo‘llar:

- project path: `/home/yourusername/diabet-AI`
- virtualenv: `/home/yourusername/.virtualenvs/diabet-heal-ai`

## 6. Production settings notes

- `DEBUG=False`
- HTTPS uchun `CSRF_TRUSTED_ORIGINS` to‘g‘ri bo‘lishi kerak
- `collectstatic` har static o‘zgarganda qayta ishga tushiriladi
- SQLite MVP uchun ishlaydi, lekin katta yuklama uchun MySQL/PostgreSQL tavsiya etiladi

## 7. Troubleshooting

- Static chiqmasa: `collectstatic` bajarganini va Web tab mapping’ini tekshiring
- Import error bo‘lsa: WSGI `sys.path` va project path mosligini tekshiring
- ALLOWED_HOSTS xatosi: domenni `.env` ichiga qo‘shing
- CSRF xatosi: `CSRF_TRUSTED_ORIGINS` ga `https://yourusername.pythonanywhere.com` ni qo‘shing
- Template topilmasa: repo ichida `templates/` saqlanganini va `DIRS` sozlanganini tekshiring

## 8. Deployment checklist

1. Repo yuklandi
2. Virtualenv yaratildi
3. Requirements o‘rnatildi
4. `.env` yaratildi
5. Migrations ishladi
6. Superuser yaratildi
7. Static mapping qilindi
8. WSGI qayta yuklandi
9. Admin va public pages tekshirildi
