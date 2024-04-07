from django.shortcuts import get_object_or_404, render

from rest_framework.views import APIView
from rest_framework.response import Response
from site_title.models import Curse
from site_title.serializer import Site_titleSerializer


class curse_detail(APIView):
    def get(self, request, curs_id):
        curse = get_object_or_404(Curse.objects.select_related(
            'location', 'trainer'
            ).filter(pk=curs_id, is_published=True)
        )
        serializer = Site_titleSerializer(curse)
        return Response(serializer.data)

    def post(self, request):
        serializer = Site_titleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
