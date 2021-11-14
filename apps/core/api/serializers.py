from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from apps.core.models import *
from apps.tiketing.models import *


class StadiomSerializer(serializers.ModelSerializer):
    en_title = serializers.CharField(max_length=255, required=False)
    fa_title = serializers.CharField(max_length=255, required=True)
    capacity = serializers.IntegerField(required=False, validators=[MinValueValidator(0)])
    seat_map_detail = serializers.JSONField(required=False, )

    class Meta:
        model = Stadiom
        fields = [
            'en_title',
            'fa_title',
            'capacity',
            'seat_map_detail',
        ]

    def create(self, validated_data):

        Stadiom.objects.create(en_title=validated_data["en_title"], fa_title=validated_data["fa_title"],
                               capacity=validated_data["capacity"])
        Layout.objects.create(stadiom=Stadiom.objects.filter(en_title=validated_data["en_title"]).first(),seat_map_detail=validated_data["seat_map_detail"])
        seat_map_data = validated_data["seat_map_detail"]
        for item in seat_map_data["map"]:

            for place in item["places"]:
                for row in range(place["rows"]):
                    for seat in range(place["seat_in_row"]):
                        SeatMapDetail.objects.create(
                            layout=Layout.objects.filter(stadiom__en_title=validated_data["en_title"]).first(),
                            seat_name="{}-{}-{}-{}".format(str(item["floor"]), str(place["place_name"]), str(row + 1),
                                                           str(seat + 1)))
        return True



class EventSerializer(serializers.ModelSerializer):
    stadiom_en_title = serializers.CharField(max_length=255, required=False)
    host_team = serializers.CharField(max_length=255, required=False)
    guest_team = serializers.CharField(max_length=255, required=True)
    event_date = serializers.DateTimeField()

    class Meta:
        model = Event
        fields = [
            'stadiom_en_title',
            'host_team',
            'guest_team',
            'event_date',
        ]

