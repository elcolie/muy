from rest_framework import serializers

from daryadi.models import PuzzleMoney


class PuzzleMoneySerializer(serializers.ModelSerializer):
    amount_currency = serializers.CharField()

    class Meta:
        model = PuzzleMoney
        fields = [
            'name',
            'amount',
            'amount_currency',
        ]
