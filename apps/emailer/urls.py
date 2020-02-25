# Django/DRF imports
from rest_framework.routers import DefaultRouter
from rest_framework import routers

# App imports
from apps.emailer.api_views import SendNotifViewSet


router = DefaultRouter()
router.register(r'send-notification', SendNotifViewSet, basename="send-notif")
urlpatterns = router.urls