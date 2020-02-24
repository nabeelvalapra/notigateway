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
5. Install RabbitMQ; Start RabbitMQ; $ rabbitmq-server
6. Rename notigateway/settings/local_settings.sample -> local_settings.py and set your local configuration.
7. python manage.py migrate
8. python manage.py runserver
9. celery -A notigateway worker -l info