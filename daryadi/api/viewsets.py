from rest_framework import viewsets

from daryadi.api.serializers import PuzzleMoneySerializer
from daryadi.models import PuzzleMoney


class PuzzleMoneyViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    queryset = PuzzleMoney.objects.all()
    serializer_class = PuzzleMoneySerializer
