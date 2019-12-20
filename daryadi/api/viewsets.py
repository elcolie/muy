from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from daryadi.api.serializers import PuzzleMoneySerializer
from daryadi.models import PuzzleMoney


class PuzzleMoneyViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    queryset = PuzzleMoney.objects.all()
    serializer_class = PuzzleMoneySerializer


class SimpleAPIViewSet(APIView):

    def get(self, request, format=None):
        return Response(data={
            'message': "Get"
        }, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        return Response(data={
            'message': "Post"
        }, status=status.HTTP_200_OK)
