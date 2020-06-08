# Turn off bytecode generation
import sys
sys.dont_write_bytecode = True

# Django specific settings
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
import django
django.setup()

# Import your models for use in your script
from db.models import *

# Start of application script (demo code below)
# for u in User.objects.all():
#	print("ID: " + str(u.id) + "\tUsername: " + u.name)

for f in File.objects.all():
	print(f)
