# SETUP REQUIRED: the path to the project's top level folder
import sys
sys.path.insert(0, '/path/to/toplevel/project/folder')

# SETUP REQUIRED: set the database configuration
from django.conf import settings
settings.configure(
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'sqlite.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
)
# Import your models for use in your script
from db.models import *

# Start your normal python script below
print MyModel.objects.all()
