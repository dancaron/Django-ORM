Django ORM Standalone Template
==============================

This is a python project template that allows you to use the database components of Django without having to use the rest of Django (i.e. running a web server). A typical use case for using this template would be if you are writing a python script and you would like the database functionality provided by Django, but have no need for the request/response functionalty of a client/server web application that Django provides. 

With this project template you can write regular python scripts and use Django's excellent ORM functionality with the database backend of your choice. This makes it convienient for Djangonauts to write database driven python applications with the familiar and well polished Django ORM. Enjoy.

Requirements
------------
- Last tested successfully with Python 3.7 and Django 3.1.2
- Create venv and pip install django to import the required modules.

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
__The models.py file is where you add your typical Django models.__ There is a toy user model included as a simple example. The db.sqlite3 file is the sample database that ships with the template. The settings.py file is where can swap out the sqlite3 database for another database connection, such as Postgres or AmazonRDS, if you wish. For most applications, sqlite3 will be powerful enough. But if you need to swap databases down the road, you can easily do so, which is one of the benefits of using the Django ORM. 

__The main.py file is the entry point for the project, and where you start your code. Think of it like a plain old python file, but now with the power of Django models.__

Quick Setup
-----------
Create a folder for your project on your local machine
```
mkdir myproject; cd myproject
```
Create a virtual environment and install django
```
python3 -m venv venv; source venv/bin/activate; pip install django
```
Download this project template from GitHub
```
git clone git@github.com:dancaron/Django-ORM.git; cd Django-ORM
```
Run the project
```
python3 main.py
```

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
