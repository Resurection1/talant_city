from rest_framework.views import APIView
from rest_framework.response import Response

from .serializer import AboutSerializer
from .models import About


class about(APIView):
    """Отрисовка страницы о проекте"""

    def get(self, request):
        about = About.objects.values(
            'title', 'text', 'photo', 'is_published').filter(is_published=True)
        serializer = AboutSerializer(about, many=True)
        return Response(serializer.data)
