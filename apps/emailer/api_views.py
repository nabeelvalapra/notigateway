# DRF imports
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

# App imports
from emailer.serializers import NotificationSerializer
from emailer.tasks import send_notif


class SendNotification(viewsets.ViewSet):
    """
    /send-notification/ accepts notification-data
    and pushes to queue for the processing.
    """
    serializer_class = NotificationSerializer
    http_method_names = ['post', ]

    def create(self, request):
        notif =  self.serializer_class(data=request.data)
        if notif.is_valid():
            notif.save()
            send_notif.delay(notif.data)
            return Response(notif.data, status=status.HTTP_206_PARTIAL_CONTENT)
        return Response(notif.error)
        

