from .base import *
from decouple import config

DEBUG = True

ALLOWED_HOSTS = ["*"]

# Database Settings
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASS"),
        "HOST": config("DB_HOST"),
        "PORT": config("DB_PORT"),
    }
}
# DJANGO SECRET KEY
SECRET_KEY = config("DJANGO_SECRET_KEY")
