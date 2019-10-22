from django.db import models


class Fauzan(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
