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

# START OF APPLICATION (demo code below)

print("Welcome to Django ORM!")
print("Now you have the power of Django's ORM at your fingertips!")
print("The sample output below is printing usernames from the User model.")

for u in User.objects.all():
	print("ID: " + str(u.id) + "\tUsername: " + u.name)
