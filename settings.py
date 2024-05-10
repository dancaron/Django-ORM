from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'sub_dir' 
BASE_DIR = Path(__file__).resolve().parent

# SECURITY WARNING: Modify this secret key if using in production!
SECRET_KEY = "6few3nci_q_o@l1dlbk81%wcxe!*6r29yu629&d97!hiqat9fa"

# Use BigAutoField for Default Primary Key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / 'db.sqlite3',
    }
}


"""
To connect to an existing postgres database, first:
pip install psycopg2
then overwrite the settings above with:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'YOURDB',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
"""

INSTALLED_APPS = ("db",)
