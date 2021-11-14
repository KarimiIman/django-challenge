from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.tiketing.api.serializers import TiketSerializer
from apps.tiketing.models import Tiket


class Tiketing(APIView):
    """
    tiketing
    """

    def post(self, request):

        serializer = TiketSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {"success": False, 'dev_message': 'wrong functionality', "message": "اطلاعات وارد شده صحیح نمیباشد",
                 'data': {'messages': serializer.errors}},
                status=status.HTTP_400_BAD_REQUEST)
        if Tiket.objects.filter(user=request.user).first():
            return Response({
                'success': False,
                'message': 'شما پیش از این بلیط این مسابقه را تهیه نموده اید',
            }, status=status.HTTP_400_BAD_REQUEST)
        tiket = Tiket.objects.filter(id=request.data["seat_id"], status=1).first()
        if tiket != None:
            tiket.status = 3
            tiket.user = request.user
            tiket.save()
            return Response({
                'success': True,
                'message': 'بلیط شما با موافقیت صادر شد',
                'dev_message': 'Success'
            },
                status=status.HTTP_200_OK)


        else:
            return Response({
                'success': False,
                'message': 'شما دسترسی ثبت یک رویداد را  در سامانه را ندارید',
            },
                status=status.HTTP_400_BAD_REQUEST)
