from decouple import config
import os

from .base import *

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
SECRET_KEY = config("SECRET_KEY")

###### Celery Configuration ###############
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_BROKER_URL = "redis://"
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_BACKEND = None
