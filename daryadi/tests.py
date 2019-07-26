from django.test import TestCase, TransactionTestCase
from model_mommy import mommy
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from daryadi.models import PuzzleMoney


class PuzzleMoneyTestCase(TransactionTestCase):
    def setUp(self) -> None:
        mommy.make(PuzzleMoney, name='THB', amount='100', amount_currency=33.0)


    def test_filter(self):
        client = APIClient()
        url = reverse()


