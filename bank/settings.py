import logging
import os

STORE_PREFIX = 'store'

DEBUG = True
BASE_DIR = os.path.dirname(__file__)

ALLOWED_HOSTS = ['hecbank.ru', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


INSTALLED_APPS = [
    "bank",
    "django.contrib.auth",
    "django.contrib.admin",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.staticfiles",
    "django.contrib.messages",
]

SECRET_KEY = 'supersikrettf1oybj9alm100im6whyg$_fz2e4xjqt=i-s4dg'
LOGIN_REDIRECT_URL = "/"


STATIC_URL = '/static/'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
# ]
STATIC_ROOT = os.path.join(BASE_DIR, "static")


ROOT_URLCONF = "bank.urls"
LANGUAGES = (("en", "English"), ("ru", "Russian"))

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(STATIC_ROOT, 'templates')
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

STRIPE_SECRET_KEY = "none"
STRIPE_PUBLISHABLE_KEY = "none"

USER_PAYMENTS = {
    "processors": [
        "user_payments.stripe_customers.processing.with_stripe_customer",
        "user_payments.processing.please_pay_mail",
    ]
}

if os.environ.get("LOG"):
    logger = logging.getLogger("user_payments")
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.DEBUG)

WSGI_APPLICATION = 'bank.wsgi.application'
