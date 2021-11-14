
from apps.users.api import views
from django.urls import path
from rest_framework_jwt.views import refresh_jwt_token

urlpatterns = [

    path('register', views.UserCreate.as_view(), name=None),
    path('login', views.Login.as_view(), name=None),
    path('refresh/token', refresh_jwt_token),
]