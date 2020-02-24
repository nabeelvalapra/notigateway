# Notification Gateway App

## Installation Instructions
1. Create Virutal Environment with Python 3.6
2. git pull 
3. pip install -r requirements.txt
4. Create Postgres DB
```
$ sudo su - postgres
$ psql
$ CREATE DATABASE notigateway;
```
5. Create a file in notigateway/settings/local_settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'notigateway',                      
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
    }
}
```
6. python manage.py migrate
7. python manage.py runserver