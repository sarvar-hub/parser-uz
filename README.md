﻿https://djangocentral.com/building-a-blog-application-with-django/

Windows Users
cd Desktop
virtualenv django
cd django
Scripts\activate.bat

Mac and Unix Users
mkdir django
cd django
python3 -m venv django
source django/bin/activate

pip install Django

cd Desktop
mkdir mysite
cd mysite

django-admin startproject mysite

cd mysite
python manage.py startapp blog

