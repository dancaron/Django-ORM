Django ORM Standalone Template
==============================

This is a python project template that allows you to use the database component of Django without having to use the rest of Django (i.e. running a web server). Now you can write regular python scripts and use Django's excellent ORM functionality with the database of your choice. This makes it convienient for Djangonauts to write database driven python applications with the familiar and well polished Django ORM. Enjoy.

Requirements
------------
- Last tested with Python 3.7 and Django 3.1.2
- You must install django so that we can import the required modules.

File Structure
--------------
```
django-orm/
├── db/
│   ├── __init__.py
│   └── models.py
├── db.sqlite3
├── main.py
├── manage.py
├── README.md
└── settings.py
```
The file structure is very simple. The models.py file is where you setup your typical Django models. db.sqlite3 is the default database that ships with the template. The main.py file is the entry point for the project, and where you start your code. The settings.py file is where can swap out the SQLITE3 database for another connection, such as Postgres or AmazonRDS. 

Quick Setup
-----------

1. pip install django
2. settings.py - (optional) edit your database settings
3. db/models.py - Add your models
4. python main.py (Run the project)

__main.py is the file where you start coding your project.__ Think of it like a plain old python file, but now with the power of Django's ORM functionality.

Feel free to send pull requests if you want to improve this project.

Django Models
-------------

Link: [How to Use Django Models](https://docs.djangoproject.com/en/3.1/topics/db/models/)

License
-------

The MIT License (MIT) Copyright (c) 2020 Dan Caron

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
