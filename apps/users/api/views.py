from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.users.api.serializers import UserSerializer, loginSerializer
from django.contrib.auth.models import User
from .trait import jWTMixin
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny


@permission_classes((AllowAny,))
class UserCreate(jWTMixin, APIView):
    """ 
    Create the user.
    """

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response({
                    'success': True,
                    'data': {'token': self.getToken(user),
                             'user_info': serializer.data,
                             },
                    'message': "به سامانه خرید بلیط رویداد های ورزشی خوش آمدید",
                    'dev_message': 'token generate'
                })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes((AllowAny,))
class Login(jWTMixin, APIView):
    """
    Login the user.
    """
    def post(self, request):
        login_serializer = loginSerializer(data=request.data)
        if not login_serializer.is_valid():
            return Response(
                {"success": False, 'dev_message': 'wrong functionality', "message": "اطلاعات وارد شده صحیح نمیباشد",
                 'data': {'messages': login_serializer.errors}},
                status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.filter(username=request.data['username']).first()
        if user is None:
            return Response({
                'success': False,
                'message': "یوزری با این نام کاربری یافت نشد",
                'dev_message': 'not found'
            }, status=status.HTTP_404_NOT_FOUND)
        if user.check_password(request.data['password']):
            token = self.getToken(user)
            return Response({
                'success': True,
                'data': {
                    'token': token,
                    'user_info': UserSerializer(user, many=False).data

                },
                'message': "ورود موفقیت آمیز به سامانه",
                'dev_message': 'token generate'

            })
        else:
            return Response({
                'success': False,
                'message': "کلمه عبور اشتباه است",
                'dev_message': 'mistake user and pass'
            }, status=status.HTTP_401_UNAUTHORIZED)
