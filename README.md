Django ORM Standalone Template

这是从dancaron的Django-ORM抽离出来的兼容python2和python3的Django-ORM系统,dancaron原有的代码基于python2.7+django 1.4.0,我复写的项目实现了对python3.4+ Django1.10.2(已测试的版本)
使用Django-ORM
- 示例：运行 python main.py可感受 Django-ORM
- 安装django
- 安装对应的数据库驱动 mysql推荐安装 mysqldb,如果使用的是mysql官方的数据库驱动：mysql-connector,则django数据库引擎需要改成 `mysql.connector.django`
- 配置settings.py文件中的数据库配置和SECRET_KEY
- 在 db/models.py里编写模型类
- 在数据库中同步数据库和表
- 在main.py及其他的地方使用Django-ORM

##### db.sqlite3是我的示例数据库，可删除


##### Fork By https://github.com/dancaron/Django-ORM
==============================

Authors - wsqy https://github.com/wsqy/Python-Django-ORM

This is a Django project template that allows you to use the database component of Django without having to use the rest of Django (i.e. running a web server). Now you can write regular python scripts and use Django's excellent database functionality.


Requirements
------------
This repository doesn't ship with a Django installation. The system must have an existing django installation so that we can safely import required modules. Developed on Python 2.7+ or 3.4+ and Django 1.10.2

Quick Setup
-----------

+ 1.) Inside settings.py - Edit your database settings
+ 2.) Inside db/models.py - Setup your models

__main.py is the file where you start coding your project.__ Think of it like a plain old python file, but now with the power of Django's database functionality! Feel free to send pull requests if you want to improve this project.
