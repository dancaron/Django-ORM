#!/usr/bin/env python
import os
import sys

sys.dont_write_bytecode = True

# SETUP REQUIRED: your full path to top level project folder
sys.path.insert(0, '/path/to/toplevel/project/folder')

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
