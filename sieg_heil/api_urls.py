from rest_framework import routers

from daryadi.api.viewsets import PuzzleMoneyViewSet
from fauzans.api.viewsets import FauzanViewSet
from questions.api.viewsets import QuestionViewSet

app_name = "apis"

router = routers.DefaultRouter()
router.register(r'daryadis', PuzzleMoneyViewSet, base_name='xxx')
router.register(r'fauzans', FauzanViewSet)
router.register(r'questions', QuestionViewSet, basename='question')
urlpatterns = router.urls
