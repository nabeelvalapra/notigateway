# DRF/Django Imports
from rest_framework import serializers

# App imports
from emailer.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
