#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    try:
        from django.core.management import execute_from_command_line
        execute_from_command_line(sys.argv)
    except Exception:
        print("Exception: Django Not Found, please install it with \"pip install django\".")
        sys.exit()
