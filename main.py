# Django specific settings
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

# Import your models for use in your script
from db.models import *

# Start of application script (demo code below)

user = User(name="Dan", email="dancaron@gmail.com")
user.save()

sample_user = User.objects.all()[0]

print sample_user.name
print sample_user.email
