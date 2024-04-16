from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Timetable, Curse
from .serializer import TimetableSerializer, CurseSerializer


class curse_detail(APIView):
    """Информация о конкретном курсе"""

    def get(self, request, curs_id):
        curse = get_object_or_404(Curse.objects.values(
            'title', 'description'
        ).filter(pk=curs_id, is_published=True)
        )
        serializer = CurseSerializer(curse)
        return Response(serializer.data)


class curse_list(APIView):
    """Список всех курсов"""

    def get(self, request):
        curse = Curse.objects.values(
            'title', 'description'
        ).filter(is_published=True)
        serializer = CurseSerializer(curse, many=True)
        return Response(serializer.data)


class timetable(APIView):
    """Отрисовка страницы с расписанием"""

    def get(self, request):
        timetable = Timetable.objects.select_related(
            'location', 'curse', 'trainer'
        ).filter(
            is_published=True,

        ).order_by(
            'introductory_lecture')
        serializer = TimetableSerializer(timetable, many=True)
        return Response(serializer.data)
