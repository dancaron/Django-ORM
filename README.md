Django ORM Standalone Template
==============================

Authors - Dan Caron, Abu Ashraf Masnun, wsqy

This is a Django project template that allows you to use the database component of Django without having to use the rest of Django (i.e. running a web server). Now you can write regular python scripts and use Django's excellent ORM functionality with the database of your choice.

Requirements
------------
This repository doesn't ship with a Django installation. The system must have an existing django installation so that we can safely import required modules. Developed on Python 2.7+ or 3.4+ and Django 1.10.2

Quick Setup
-----------

1.) pip install django
2.) Inside settings.py - Edit your database settings (sqlite3 setup by default)
3.) Inside db/models.py - Add your models (Basic user model setup by default)
4.) python main.py (Run the project)

__main.py is the file where you start coding your project.__ Think of it like a plain old python file, but now with the power of Django's ORM functionality! Feel free to send pull requests if you want to improve this project.

Django Models
-------------

Link: [How to use Django Models](https://docs.djangoproject.com/en/1.10/topics/db/models/)
