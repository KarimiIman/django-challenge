
from apps.tiketing.api import views
from django.urls import path

urlpatterns = [

    path('tiketing', views.Tiketing.as_view(), name=None),
]