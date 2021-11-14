from rest_framework import serializers
from apps.tiketing.models import *


class TiketSerializer(serializers.ModelSerializer):
    seat_id = serializers.IntegerField(required=True)

    class Meta:
        model = Tiket
        fields = [
            'seat_id',
        ]
