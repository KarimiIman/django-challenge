
from apps.core.api import views
from django.urls import path

urlpatterns = [
    path('stadiom', views.StadiomCreate.as_view(), name=None),
    path('event', views.EventCreate.as_view(), name=None),
]