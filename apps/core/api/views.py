from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.core.api.serializers import StadiomSerializer, EventSerializer
from django.contrib.auth.models import User
from apps.core.models import *
from apps.tiketing.models import Tiket


class StadiomCreate(APIView):
    """
    Create Stadiom
    """

    def post(self, request):
        if User.objects.filter(groups__name='stadiom_creators', username=request.user.username).exists():
            serializer = StadiomSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(
                    {"success": False, 'dev_message': 'wrong functionality', "message": "اطلاعات وارد شده صحیح نمیباشد",
                     'data': {'messages': serializer.errors}},
                    status=status.HTTP_400_BAD_REQUEST)
            stadiom = serializer.save()
            return Response({
                'success': True,
                'message': 'استادیوم با موفقیت ساخته شد',
                'dev_message': 'Success'
            },
                status=status.HTTP_200_OK)

        else:
            return Response({
                'success': False,
                'message': 'شما دسترسی ساخت یک استادیوم در سامانه را ندارید',
                'dev_message': 'Not Permitted'
            },
                status=status.HTTP_403_FORBIDDEN)


class EventCreate(APIView):
    """
    Create Event
    """

    def post(self, request):
        if User.objects.filter(groups__name='event_creators', username=request.user.username).exists():
            serializer = EventSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(
                    {"success": False, 'dev_message': 'wrong functionality', "message": "اطلاعات وارد شده صحیح نمیباشد",
                     'data': {'messages': serializer.errors}},
                    status=status.HTTP_400_BAD_REQUEST)
            stadiom = Stadiom.objects.filter(en_title=request.data["stadiom_en_title"]).first()
            Event.objects.create(
                stadiom=stadiom,
                host_team=request.data["host_team"],
                guest_team=request.data["guest_team"],
                event_date=request.data["event_date"])
            stadiom_seats = SeatMapDetail.objects.filter(layout__stadiom=stadiom)
            for seat in stadiom_seats:
                Tiket.objects.create(
                    event=Event.objects.filter(stadiom=stadiom,
                                               host_team=request.data["host_team"],
                                               guest_team=request.data["guest_team"],
                                               event_date=request.data["event_date"]).first(),
                    seat=seat, )

            return Response({
                'success': True,
                'message': 'رویداد با موفقیت ثبت گردید',
                'dev_message': 'Success'
            },
                status=status.HTTP_200_OK)

        else:
            return Response({
                'success': False,
                'message': 'شما دسترسی ثبت یک رویداد را  در سامانه را ندارید',
                'dev_message': 'Not Permitted'
            },
                status=status.HTTP_403_FORBIDDEN)
