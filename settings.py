import os

import environ

env = environ.Env()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# SECURITY WARNING: Modify this secret key if using in production!
SECRET_KEY = "6few3nci_q_o@l1dlbk81%wcxe!*6r29yu629&d97!hiqat9fa"
DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
]
LOCAL_APPS = [
    "apps.core",
    "apps.users",
    "apps.videos",
    "apps.youtube",
]
THIRD_PARTY_APPS = ["django_extensions"]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# https://docs.djangoproject.com/en/dev/ref/settings/#auth-user-model
AUTH_USER_MODEL = "users.User"

# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {"default": env.db("DATABASE_URL")}
DATABASES["default"]["ATOMIC_REQUESTS"] = True

# python-youtube: https://github.com/sns-sdks/python-youtube
# ------------------------------------------------------------------------------
YOUTUBE_DATA_API_KEY = env.str(
    "YOUTUBE_DATA_API_KEY", default="GhkQWNUNqki2yk79dtCwDi"
)  # noqa
