from django.db import models


class Candy(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
