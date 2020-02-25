# django imports
from django.core.mail import send_mail
from django.conf import settings

# Celery import 
from celery import shared_task

# App imports
from emailer.models import Notification


@shared_task
def send_notif(notif_data):
    send_mail(
        notif_data['subject'],
        notif_data['body'],
        settings.EMAIL_HOST_USER,
        [notif_data['recipient']]
    )

    notif = Notification.objects.get(id=notif_data['id'])
    notif.has_send = True
    notif.save()


