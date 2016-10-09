# Django specific settings
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
import django
django.setup()
# Import your models for use in your script
from db.models import *

# Start of application script (demo code below)
user = User.objects.get(id=1)
print(user.name)
