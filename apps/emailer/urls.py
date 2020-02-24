# Django/DRF imports
from rest_framework import routers

# App imports
from apps.emailer.api_views import SendNotification


router = routers.SimpleRouter()
router.register(r'send-notification', SendNotification, basename='send-notification')

urlpatterns = router.urls