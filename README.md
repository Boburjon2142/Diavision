# DiaVision AI

DiaVision AI bu Django asosidagi, mobil-first, AI va IoT ko‘rinishi aniq seziladigan diabet profilaktikasi va monitoring platformasi. Interfeys va copywriting to‘liq o‘zbek tilida tayyorlangan, AI esa izohlanadigan rule-based service layer orqali ishlaydi.

## 1. Product concept summary

- Maqsad: diabet xavfini erta aniqlash, qon shakarini kuzatish va AI tavsiyalar bilan foydalanuvchini qo‘llab-quvvatlash.
- UX pozitsiyasi: rasmiy, tibbiy mas’uliyatli, premium public-health uslub.
- AI ko‘rinishi: homepage, dashboard, tracker, food assistant, reports va alerts bo‘limlarida ochiq ko‘rinadi.
- Deployment: PythonAnywhere uchun oddiy Django + SQLite MVP, keyin PostgreSQL’ga moslashtiriladigan struktura.

## 2. Full project folder structure

```text
diabet-AI/
|-- manage.py
|-- requirements.txt
|-- .env.example
|-- README.md
|-- DEPLOYMENT_PYTHONANYWHERE.md
|-- sample_data.json
|-- diabet_heal_ai/
|   |-- settings.py
|   |-- urls.py
|   |-- wsgi.py
|   |-- asgi.py
|   `-- pythonanywhere_wsgi.py
|-- core/
|-- accounts/
|-- pages/
|-- dashboard/
|-- riskcheck/
|-- tracker/
|-- reminders/
|-- nutrition/
|-- reports/
|-- adminpanel/
|-- ai_engine/
|-- templates/
`-- static/
```

## 3. Database model plan

- `accounts.UserProfile`: foydalanuvchi sog‘liq va kontakt profili.
- `riskcheck.RiskAssessment`: asosiy risk snapshot.
- `riskcheck.RiskFactorDetail`: AI aniqlagan omillar.
- `tracker.SugarReading`: qon shakari yozuvlari.
- `reminders.Reminder`: smart reminder CRUD.
- `nutrition.FoodQueryHistory`: AI oziq-ovqat tahlili tarixi.
- `reports.HealthReport`: haftalik va oylik hisobotlar uchun model.
- `reports.AlertLog`: signal va ogohlantirishlar.
- `pages.DoctorRequest`: doctor connect so‘rovlari.
- `pages.Article`: profilaktika maqolalari.
- `pages.FAQ`: FAQ yozuvlari.
- `reports.AIInsightLog`: AI insight timeline uchun log.
- `reports.LifestyleScoreSnapshot`: lifestyle score snapshot.

## 4. URL map

- `/` bosh sahifa
- `/about/`, `/tips/`, `/faq/`, `/contact/`, `/doctor-connect/`
- `/risk/` public AI risk check
- `/risk/new/` authenticated assessment
- `/tracker/`, `/tracker/list/`, `/tracker/new/`
- `/reminders/`, `/reminders/new/`
- `/nutrition/`, `/nutrition/history/`
- `/reports/`, `/reports/dashboard/`, `/reports/print/<period>/`
- `/dashboard/`
- `/management/`
- `/admin/`
- `/ai/health/`

## 5. Key service layer design

- `ai_engine/services/risk_engine.py`: qoidaviy risk score + explanation.
- `ai_engine/services/food_engine.py`: taom tahlili va alternativalar.
- `ai_engine/services/trend_engine.py`: shakar trend insight.
- `ai_engine/services/habit_engine.py`: reminder optimization va lifestyle score.
- `ai_engine/services/alert_engine.py`: signal / ogohlantirish logikasi.
- `ai_engine/services/explanation_engine.py`: tavsiya matnlari uchun helper.

UI aynan shu servis natijalariga tayanganligi sabab keyin ML model bilan almashtirish oson.

## 6. Django settings structure

- `.env` orqali `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, `CSRF_TRUSTED_ORIGINS`
- `STATIC_ROOT` va `STATICFILES_DIRS` PythonAnywhere uchun tayyor
- SQLite default, keyin PostgreSQL uchun `DATABASES` almashtiriladi
- `core.context_processors.platform_context` orqali global microcopy va nav

## 7-15. Models, forms, views, URLs, templates, CSS, JS, admin, AI logic

Bu qatlamlar app kesimida alohida fayllarda yozilgan:

- [accounts/models.py](/c:/Users/Omen/Desktop/diabet-AI/accounts/models.py)
- [pages/views.py](/c:/Users/Omen/Desktop/diabet-AI/pages/views.py)
- [riskcheck/services.py](/c:/Users/Omen/Desktop/diabet-AI/riskcheck/services.py)
- [tracker/views.py](/c:/Users/Omen/Desktop/diabet-AI/tracker/views.py)
- [reminders/views.py](/c:/Users/Omen/Desktop/diabet-AI/reminders/views.py)
- [nutrition/services.py](/c:/Users/Omen/Desktop/diabet-AI/nutrition/services.py)
- [reports/services.py](/c:/Users/Omen/Desktop/diabet-AI/reports/services.py)
- [dashboard/views.py](/c:/Users/Omen/Desktop/diabet-AI/dashboard/views.py)
- [templates/pages/home.html](/c:/Users/Omen/Desktop/diabet-AI/templates/pages/home.html)
- [static/css/app.css](/c:/Users/Omen/Desktop/diabet-AI/static/css/app.css)

## 16. Sample data

- `sample_data.json` ichida `Article` va `FAQ` uchun boshlang‘ich fixture mavjud.
- `python manage.py loaddata sample_data.json` orqali yuklash mumkin.

## 17. Deployment guide for PythonAnywhere

To‘liq qo‘llanma: [DEPLOYMENT_PYTHONANYWHERE.md](/c:/Users/Omen/Desktop/diabet-AI/DEPLOYMENT_PYTHONANYWHERE.md)

## 18. Final run checklist

1. Virtualenv yarating va `pip install -r requirements.txt`.
2. `.env.example` dan `.env` yarating.
3. `python manage.py makemigrations`
4. `python manage.py migrate`
5. `python manage.py loaddata sample_data.json`
6. `python manage.py createsuperuser`
7. `python manage.py collectstatic`
8. `python manage.py runserver`
