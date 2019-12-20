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

    def post(self, request, format=None):
        """
        SCB callback example
        {
          'payeeProxyId': '625534193160056',
          'payeeProxyType': 'BILLERID',
          'payeeAccountNumber': '0987654321',
          'payeeName': 'Ming Sama',
          'payerProxyId': '0812345678',
          'payerProxyType': 'MSISDN',
          'payerAccountNumber': '1412890001',
          'payerName': 'Juli Chugsakon',
          'sendingBankCode': '014',
          'receivingBankCode': '014',
          'amount': '150',
          'channelCode': 'PMH',
          'transactionId': '20191220526NcwMVe3v1TcW',
          'transactionDateandTime': '2019-12-20T19:12:03+07:00',
          'billPaymentRef1': 'D72568249FC1432181FD',
          'billPaymentRef2': '2FD70D4444064691A20B',
          'billPaymentRef3': 'MIN',
          'currencyCode': '764',
          'transactionType': 'Domestic Transfer'
        }
        :param request:
        :param format:
        :return:
        """
        return Response(data={
            'message': "Good Day"
        }, status=status.HTTP_200_OK)
