from rest_framework import serializers

from fauzans.models import Fauzan


class FauzanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fauzan
        fields = (
            'name',
        )
