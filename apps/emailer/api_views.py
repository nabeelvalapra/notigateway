# Django imports
from django.shortcuts import get_object_or_404

# DRF imports
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

# App imports
from emailer.models import Notification
from emailer.serializers import NotificationSerializer
from emailer.tasks import send_notif


class SendNotifViewSet(viewsets.ViewSet):
    """
    /send-notification/ accepts notification-data
    and pushes to queue for the processing.
    """
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def create(self, request):
        notif =  self.serializer_class(data=request.data)
        if notif.is_valid():
            notif.save()
            send_notif.delay(notif.data)
            return Response(notif.data, status=status.HTTP_206_PARTIAL_CONTENT)
        return Response(notif.error)

    def retrieve(self, request, pk=None):
        notif = get_object_or_404(self.queryset, pk=pk)            
        notif_ser = NotificationSerializer(notif)
        return Response(notif_ser.data)