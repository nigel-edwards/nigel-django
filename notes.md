# These are my Django Notes

Checking connection with Git

[Install Python](https://www.python.org/downloads/) 3.9.6
Install django pip install --user django==3.0.3 best installed as admin

Create new project
1. navigate to project directory in terminal
2.  `django-admin startproject "projectname"`

Creates a folder called projectname which contains

  - manage.py - scripts used to manage the project
  - projectname/__init__.py - dunder init
  - projectname/asgi.py - hooks for web servers such as apache
  - *projectname/settings.py - configures Django*
  - *projectname/urls.py  - routes requests based on URL*
  - projectname/wsgi.py - hooks for web servers such as apache

## Running for first time

- Navigate to project directory, check in correct place should be same level as manage.py
- type `python manage.py runserver`
- Should see the server running at it's portnumber : "Starting development server at http://127.0.0.1:8000/"
- Should be able to browse to that site and wee a welcome message.