from django.db import models
from apps.core.models import Event,SeatMapDetail
from django.contrib.auth.models import User

class Status(models.IntegerChoices):
    deactive= 0,
    free = 1,
    reserved = 2,
    sold = 3,

class Tiket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="event" )
    seat = models.ForeignKey(SeatMapDetail, on_delete=models.CASCADE, related_name="seat" )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="user" )
    status = models.IntegerField(choices=Status.choices,default=1)

    def __str__(self):
        return str(self.user)+", "+str(self.event)