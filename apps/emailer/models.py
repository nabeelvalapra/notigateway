from django.db import models


class Action(models.TextChoices):
    SAVE = 'SV', 'Save'
    LOGGING = 'LG', 'Logging'
    DELIVERY = 'DV', 'Delivery'
    POST_DELIVERY = 'PD', 'Post Delivery Status'
    REPORT_GEN  = 'RD', 'Report Generation'


class Notification(models.Model):
    action = models.CharField(max_length=2, choices=Action.choices)
    recipient = models.EmailField()
    subject = models.TextField()
    body = models.TextField()
    has_send = models.BooleanField(default=False)

    class Meta:
        db_table = 'notification'



