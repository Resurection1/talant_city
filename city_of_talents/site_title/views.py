from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Curse
from .serializer import Site_titleSerializer


class site_title(APIView):
    def get(self, request):
        curses = Curse.objects.select_related(
            'location', 'trainer'
        ).filter(
            is_published=True,
        ).order_by('-pub_date')

        serializer = Site_titleSerializer(curses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Site_titleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
