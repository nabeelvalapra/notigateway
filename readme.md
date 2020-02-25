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

## Code Overview
/send-notification/ endpoint collects the data to send email. Saves this data in the model with has_send=False. Then pass on the sending task to RabbitMQ. The celery worker picks up the task, executes it and updates the model object with has_send=True

## API Doc
DRF Browsable API is enabled.
```
Endpoint: POST http://localhost:8000/api/v1/send-notification/
Description: This endpoint will register a task to send the email.
Payload: 
{
	"action": "SV",
	"recipient": "nabeel@gmail.com",
	"subject": "Hello, How's the subject",
	"body": "This is the content of this email"
}
Params:
Action: https://github.com/nabeelvalapra/notigateway/blob/master/apps/emailer/models.py#L4
```
```
Endpoint: GET http://localhost:8000/api/v1/send-notification/<pk>/
Description: Retrives the notification detail with the status(has_send)
```
