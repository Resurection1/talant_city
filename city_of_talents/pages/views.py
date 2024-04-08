from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from site_title.serializer import Site_titleSerializer
from .serializer import AboutSerializer
from site_title.models import Curse
from .models import About


class timetable(APIView):
    """Отрисовка страницы с расписанием"""

    def get(self, request):
        curses = Curse.objects.select_related('location')
        serializer = Site_titleSerializer(curses, many=True)
        return Response(serializer.data)


class about(APIView):
    """Отрисовка страницы о проекте"""

    def get(self, request):
        about = About.objects.all()
        serializer = AboutSerializer(about, many=True)
        return Response(serializer.data)
