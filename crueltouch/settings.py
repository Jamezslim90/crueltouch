"""
Django's settings for Maxify Appointment' project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

from dotenv import load_dotenv
from django.conf import global_settings

# Add custom languages not provided by Django
from django.conf import locale
from django.utils.translation import gettext_lazy as _

load_dotenv()
allowed_hosts_str = os.getenv('LIST_OF_ALLOWED_HOSTS', default="")

debug_value = os.getenv('DEBUG_VALUE')
secret_key_value = os.getenv('SECRET_KEY_VALUE')

if not debug_value or not secret_key_value:
    from crueltouch.productions import production_debug, production_secret_key
    debug_value = production_debug
    secret_key_value = production_secret_key

ADMIN_EMAIL = os.getenv('ADMIN_EMAIL', default="")
ADMIN_NAME = os.getenv('ADMIN_NAME', default="")
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', default="")
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', default="")
LIST_OF_ALLOWED_HOSTS = allowed_hosts_str.split(',') if allowed_hosts_str else []
OTHER_ADMIN_EMAIL = os.getenv('OTHER_ADMIN_EMAIL', default="")
PAYPAL_CLIENT_ID = os.getenv('PAYPAL_CLIENT_ID', default="")
PAYPAL_CLIENT_SECRET = os.getenv('PAYPAL_CLIENT_SECRET', default="")
PAYPAL_ENVIRONMENT = os.getenv('PAYPAL_ENVIRONMENT', default="")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secret_key_value

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = debug_value

ALLOWED_HOSTS = ["*"] if DEBUG else LIST_OF_ALLOWED_HOSTS

AUTH_USER_MODEL = 'client.UserClient'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django.contrib.sites",
    "django.contrib.sitemaps",
    'django.contrib.humanize',
    'homepage',
    'client',
    'static_pages_and_forms',
    'portfolio',
    'administration',
    'appointment',
    'django_q',
    'payment',
    'captcha',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.admindocs.middleware.XViewMiddleware',
    'homepage.middleware.CacheControlMiddleware'
]

ROOT_URLCONF = 'crueltouch.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'crueltouch.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#   'default': {
#     'ENGINE': 'django.db.backends.postgresql',
#     'NAME': 'central contractors ltd',
#     'USER': 'jamezslim90',
#     'PASSWORD': 'zmgHh7aNwQk9',
#     'HOST': 'ep-cold-leaf-25567838.us-west-2.aws.neon.tech',
#     'PORT': '5432',
#   }
# }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

if DEBUG:
    STATICFILES_DIRS = [
        BASE_DIR / "static",
    ]

if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = 'static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Message storage
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

# Number of seconds of inactivity before a user is marked offline
USER_ONLINE_TIMEOUT = 300

# Number of seconds that we will keep track of inactive users for before
# their last seen is removed from the cache
USER_LAST_SEEN_TIMEOUT = 60 * 60 * 24 * 7

# Caches settings
CACHES_LOCATION = os.path.join(BASE_DIR, '.cache') if DEBUG else "/home/ubuntu/.cache/crueltouch"

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': CACHES_LOCATION,
    }
}

# Email settings
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = EMAIL_HOST_USER
# EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD
# EMAIL_USE_TLS = True
# EMAIL_SUBJECT_PREFIX = ""
# EMAIL_USE_LOCALTIME = True
# SERVER_EMAIL = EMAIL_HOST_USER

ADMINS = [
    ('Adams', ADMIN_EMAIL),
]
if not DEBUG:
    ADMINS.append(('Roos', OTHER_ADMIN_EMAIL))

MANAGERS = [
    ('Adams', ADMIN_EMAIL),
]

ADMIN_EMAIL = ADMIN_EMAIL

# Language translation settings

EXTRA_LANG_INFO = {
    'cr-ht': {
        'bidi': False,  # right-to-left
        'code': 'cr-ht',
        'name': 'Haitian Creole',
        'name_local': "Kreyòl",
    },
}

LANG_INFO = dict(locale.LANG_INFO, **EXTRA_LANG_INFO)
locale.LANG_INFO = LANG_INFO

LANGUAGES = (
    ('en', _('English')),
    ('es', _('Spanish')),
    ('fr', _('French')),
)

# Languages using BiDi (right-to-left) layout
LANGUAGES_BIDI = global_settings.LANGUAGES_BIDI + ["cr-ht"]

LOCALE_PATHS = (
    os.path.join(BASE_DIR / 'locale'),
)

if not DEBUG:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        "handlers": {
            "file": {
                "level": "DEBUG",
                "class": "logging.FileHandler",
                "filename": "/home/ubuntu/web/crueltouch/logs/django/debug.log",
            },
        },
        'loggers': {
            "django": {
                "handlers": ["file"],
                "level": "INFO",
                "propagate": True,
            },
        },
    }

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_TZ = True

USE_L10N = True

# Extra deployment parameters
if not DEBUG:
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True

    SECURE_HSTS_SECONDS = 60
    SECURE_HSTS_PRELOAD = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True

    SESSION_EXPIRE_AT_BROWSER_CLOSE = True
    SESSION_COOKIE_AGE = 3600  # 1 hour

LOGIN_URL = 'client/login/'
LOGIN_REDIRECT_URL = 'client/'

# The number of seconds a password reset link is valid for (in second)
PASSWORD_RESET_TIMEOUT = 3600  # 1 hour

APPOINTMENT_SLOT_DURATION = 30  # minutes
APPOINTMENT_LEAD_TIME = (9, 0)  # (hour, minute) 24-hour format
APPOINTMENT_FINISH_TIME = (16, 30)  # (hour, minute) 24-hour format

# Additional configuration options
APPOINTMENT_CLIENT_MODEL = AUTH_USER_MODEL
APPOINTMENT_BASE_TEMPLATE = 'homepage/base.html'
APPOINTMENT_ADMIN_BASE_TEMPLATE = 'administration/base.html'
APPOINTMENT_WEBSITE_NAME = 'Maxify Global'
# APPOINTMENT_PAYMENT_URL = 'payment:payment_linked'
APPOINTMENT_THANK_YOU_URL = None

PAYMENT_PAYPAL_ENVIRONMENT = PAYPAL_ENVIRONMENT
PAYMENT_PAYPAL_CLIENT_ID = PAYPAL_CLIENT_ID
PAYMENT_PAYPAL_CLIENT_SECRET = PAYPAL_CLIENT_SECRET

PAYMENT_BASE_TEMPLATE = 'homepage/base.html'
PAYMENT_WEBSITE_NAME = 'Maxify'  # or your website name
PAYMENT_MODEL = 'appointment.PaymentInfo'  # Replace with your app and model name
PAYMENT_REDIRECT_SUCCESS_URL = 'homepage:index'  # Replace with your app and success view name

PAYMENT_APPLY_PAYPAL_FEES = True
PAYMENT_FEES = 0.03 if not PAYMENT_APPLY_PAYPAL_FEES else 0.00

PDF_CERTIFICATE_PATH = os.path.join(BASE_DIR, 'crueltouch', 'secrets', 'pdf_certificate.pfx')
CERTIFICATE_PATH = os.path.join(BASE_DIR, 'crueltouch', 'secrets', 'pdf_certificate.crt')
PRIVATE_KEY_PATH = os.path.join(BASE_DIR, 'crueltouch', 'secrets', 'pdfkey.key')

Q_CLUSTER = {
    'name': 'DjangORM',
    'workers': 4,
    'timeout': 90,
    'retry': 120,
    'queue_limit': 50,
    'bulk': 10,
    'orm': 'default',
}
