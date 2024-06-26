from datetime import datetime

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Timetable, Curse, Video,  Reviews
from .serializer import (TimetableSerializer,
                         CurseSerializer,
                         Sign_up_for_a_courseSerializer,
                         VideoSerializer,
                         Sign_up_for_a_course, ReviewsSerializer)


class curse_detail(APIView):
    """Информация о конкретном курсе"""

    def get(self, request, curs_id):
        curse = get_object_or_404(Curse.objects.all().filter(
            pk=curs_id, is_published=True
        )
        )
        serializer = CurseSerializer(curse, context={'request': request})
        return Response(serializer.data)


class curse_list(APIView):
    """Список всех курсов"""

    def get(self, request):
        curse = Curse.objects.all().filter(is_published=True)
        serializer = CurseSerializer(
            curse,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)


class timetable(APIView):
    """Отрисовка страницы с расписанием"""

    def get(self, request):
        current_date = datetime.now().date()
        timetable = Timetable.objects.select_related(
            'location', 'curse', 'trainer'
        ).filter(
            is_published=True,
            pub_date__date__lte=current_date,
        ).order_by(
            'introductory_lecture')

        serializer = TimetableSerializer(timetable, many=True)
        return Response(serializer.data)


class sign_up_for_a_course(APIView):
    """Отправка post запроса с регистрацией на курс"""
    # def get(self, request):
    #     timetable = Sign_up_for_a_course.objects.all()

    #     serializer = Sign_up_for_a_courseSerializer(timetable, many=True)
    #     return Response(serializer.data)

    def post(self, request):
        # Assuming you have a serializer for handling POST data
        serializer = Sign_up_for_a_courseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class video_list(APIView):
    """Выводит список видео"""
    def get(self, request):
        video = Video.objects.all().filter(is_published=True)

        serializer = VideoSerializer(video,
                                     many=True,
                                     context={'request': request})
        return Response(serializer.data)


class reviews(APIView):
    """Выводит отзывы"""
    def get(self, request):
        review = Reviews.objects.all().filter(is_published=True)

        serializer = ReviewsSerializer(
            review,
            many=True,
            context={'request': request})
        return Response(serializer.data)
