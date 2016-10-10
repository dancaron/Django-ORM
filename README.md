Django ORM Standalone Template
==============================

Authors - Dan Caron, Abu Ashraf Masnun, wsqy

This is a Django project template that allows you to use the database component of Django without having to use the rest of Django (i.e. running a web server). Now you can write regular python scripts and use Django's excellent ORM functionality with the database of your choice.

Requirements
------------
This repository doesn't ship with a Django installation. The system must have an existing django installation so that we can safely import required modules. Developed on Python 2.7+ or 3.4+ and Django 1.10.2

Quick Setup
-----------

* 1.) pip install django
* 2.) Inside settings.py - Edit your database settings (sqlite3 setup by default)
* 3.) Inside db/models.py - Add your models (Basic user model setup by default)
* 4.) python main.py (Run the project)

__main.py is the file where you start coding your project.__ Think of it like a plain old python file, but now with the power of Django's ORM functionality! Feel free to send pull requests if you want to improve this project.

Django Models
-------------

Link: [How to use Django Models](https://docs.djangoproject.com/en/1.10/topics/db/models/)

License
-------

The MIT License (MIT) Copyright (c) 2016 Dan Caron

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
