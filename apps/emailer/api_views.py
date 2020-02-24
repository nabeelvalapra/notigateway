# DRF imports
from rest_framework import viewsets
from rest_framework.response import Response

# App imports
from emailer.serializers import NotificationSerializer


class SendNotification(viewsets.ViewSet):
    """
    /api/v1/send-notification/ accepts notification-data
    and pushes to queue for the processing.
    """
    serializer_class = NotificationSerializer
    http_method_names = ['post', ]

    def create(self, request):
        return Response({})
        

