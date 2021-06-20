from dotenv import load_dotenv

from .base import *

DEBUG = True
ALLOWED_HOSTS = ["*"]

# Database Settings
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": load_dotenv("DB_NAME"),
        "USER": load_dotenv("DB_USER"),
        "PASSWORD": load_dotenv("DB_PASS"),
        "HOST": load_dotenv("DB_HOST"),
        "PORT": load_dotenv("DB_PORT"),
    }
}
# DJANGO SECRET KEY
SECRET_KEY = load_dotenv("SECRET_KEY")

###### Celery Configuration ###############
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TIMEZONE = TIME_ZONE
CELERY_BROKER_URL = "redis://"
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_BACKEND = None
