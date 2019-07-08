from rest_framework import routers

from fauzans.api.viewsets import FauzanViewSet

app_name = "apis"

router = routers.DefaultRouter()
router.register(r'fauzans', FauzanViewSet)
urlpatterns = router.urls
