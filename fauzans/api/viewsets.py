from rest_framework import viewsets

from fauzans.api.serializers import FauzanSerializer
from fauzans.models import Fauzan


class FauzanViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    queryset = Fauzan.objects.all()
    serializer_class = FauzanSerializer
