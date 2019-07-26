from django.db import models
from djmoney.models.fields import MoneyField


class PuzzleMoney(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    amount = MoneyField(decimal_places=2, default_currency='USD', max_digits=14)
