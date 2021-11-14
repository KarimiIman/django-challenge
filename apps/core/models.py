import jsonfield
from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


class Stadiom(models.Model):
    en_title = models.CharField(max_length=255, )
    fa_title = models.CharField(max_length=255, )
    capacity = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.en_title


class Layout(models.Model):
    stadiom = models.ForeignKey(Stadiom, on_delete=models.CASCADE, )
    seat_map_detail = jsonfield.JSONField()
    enable = models.BooleanField(default=True)

    def __str__(self):
        return self.stadiom.en_title


class SeatMapDetail(models.Model):
    layout = models.ForeignKey(Layout, on_delete=models.CASCADE, related_name="layout" )
    seat_name = models.CharField(max_length=255, )
    enable = models.BooleanField(default=True)

    def __str__(self):
        return self.seat_name


class Event(models.Model):
    stadiom= models.ForeignKey(Stadiom, on_delete=models.SET_NULL,null=True, related_name="stadiom" )
    host_team = models.CharField(max_length=255, )
    guest_team = models.CharField(max_length=255, )
    event_date = models.DateTimeField(null=True,blank=True)


    def __str__(self):
        return self.host_team +"-"+self.guest_team