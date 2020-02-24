# django imports
from django.core.mail import send_mail
from django.conf import settings


def send_notif(notif_data):
    send_mail(
        notif_data['subject'],
        notif_data['body'],
        settings.FROM_ADDRESS,
        [notif_data['recipient']],
        fail_silently=False,
    )