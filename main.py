# Turn off bytecode generation
import sys

sys.dont_write_bytecode = True

import create_aip_mets

# Django specific settings
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

import django

django.setup()

# Import your models for use in your script
from main.models import *

# Start of application script (demo code below)
# for u in User.objects.all():
# 	print("ID: " + str(u.id) + "\tUsername: " + u.name)

# for f in File.objects.all():
# 	print(f)

import traceback
from contextlib import contextmanager


class Jobs(object):
    def __init__(self, name, uuid, args, caller_wants_output=False):
        self.args = [name] + args
        self.int_code = 0
        self.status_code = "success"
        self.output = ""
        self.error = ""

    def set_status(self, int_code, status_code="success"):
        if int_code:
            self.int_code = int(int_code)
        self.status_code = status_code

    def write_output(self, s):
        self.output += s

    def write_error(self, s):
        self.error += s

    def print_error(self, *args):
        self.write_error(" ".join([self._to_str(x) for x in args]) + "\n")

    def pyprint(self, *objects, **kwargs):
        file = kwargs.get("file", sys.stdout)
        sep = kwargs.get("sep", " ")
        end = kwargs.get("end", "\n")
        msg = sep.join([self._to_str(x) for x in objects]) + end
        if file == sys.stdout:
            self.write_output(msg)
        elif file == sys.stderr:
            self.write_error(msg)
        else:
            raise Exception("Unrecognised print file: " + str(file))

    @staticmethod
    def _to_str(thing):
        try:
            return str(thing)
        except UnicodeEncodeError:
            return thing.encode("utf8")

    @contextmanager
    def JobContext(self, logger=None):
        try:
            yield
        except Exception as e:
            self.write_error(str(e))
            self.write_error(traceback.format_exc())
            self.set_status(1)


# basedir = /var/archivematica/sharedDirectory/watchedDirectories/workFlowDecisions/metadataReminder/123-d2906daf-9205-4e11-907c-77b02622b74f/
# xmlfile = /var/archivematica/sharedDirectory/watchedDirectories/workFlowDecisions/metadataReminder/123-d2906daf-9205-4e11-907c-77b02622b74f/METS.d2906daf-9205-4e11-907c-77b02622b74f.xml

output_mets_file = "metsout/METS.12345.xml"

args_example = [
    "--amdSec",
    "--baseDirectoryPath",
    "metsout",
    "--baseDirectoryPathString",
    "SIPDirectory",
    "--fileGroupIdentifier",
    "20fb8d59-c031-40ec-b08d-83a70f2eee69",
    "--fileGroupType",
    "sip_id",
    "--xmlFile",
    output_mets_file,
    "--sipType",
    "SIP",
]

job = Jobs(name="create_mets", uuid="12345", args=args_example)
jobs = [job]

create_aip_mets.call(jobs)
print(job.error)
print(job.status_code)
print("If success then METS should be partially or completely at", output_mets_file)
