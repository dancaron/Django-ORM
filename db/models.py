import sys

try:
    from django.db import models
except  Exception:
    print "There was an error loading django modules. Do you have django installed?"
    sys.exit()

# Sample User model
class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
