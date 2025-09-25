# import django_heroku
# import dj_database_url
# iot_project/settings.py
import os
from pathlib import Path
import pymysql
import dj_database_url
pymysql.install_as_MySQLdb()



# settings.py

# ---------------------------
# Authentication Settings
# ---------------------------
LOGIN_URL = "/login/"        # agar user login nahi hai toh yeh page dikhega
LOGOUT_REDIRECT_URL = "/login/"  # logout ke baad redirect yahan hoga

# Existing settings...

# If you're using the modern Django style:
BASE_DIR = Path(__file__).resolve().parent.parent


# django_heroku.settings(locals())
SECRET_KEY = 'django-insecure-your-secret-key'
DEBUG = True
ALLOWED_HOSTS = ["iot-web.onrender.com", "*"]

CSRF_TRUSTED_ORIGINS = [
    "https://16de7fd271a3.ngrok-free.app",   # tumhari current ngrok URL
]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'iot_api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",  # static files ke liye
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'iot_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'iot_api' / 'templates'],  # ← Path object
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'iot_project.wsgi.application'

# SQLite
'''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}'''
DATABASES = {
    "default": dj_database_url.config(default=os.getenv("postgresql://airkpi_mclp_user:cbAT63ju7Y0A5kmAACIOimsc0x5ceZIj@dpg-d3acrta4d50c73d5v8u0-a/airkpi_mclp"))
}

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny"
    ]
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "testwebservice71@gmail.com" 
EMAIL_HOST_PASSWORD = "akuu vulg ejlg ysbt"  

TWILIO_ACCOUNT_SID = '721caf7fd9f3071ACc3786c5763f4cd1d8'
TWILIO_AUTH_TOKEN = 'a364782f1c2ea9b02b1e30915505043d'
TWILIO_PHONE_NUMBER = '+17755877724'  # Twilio se mila number

# Static files settings for Heroku
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Activate Django-Heroku.
# django_heroku.settings(locals())
