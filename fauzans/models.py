from django.contrib.postgres.fields import JSONField
from django.db import models


class Fauzan(models.Model):
    name = JSONField()
    label = models.CharField(max_length=20, null=True, blank=True)
