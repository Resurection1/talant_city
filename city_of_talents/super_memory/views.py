from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Super_memory
from .serializer import Super_memorySerializer


class super_memory(APIView):
    def get(self, request):
        super_memory = Super_memory.objects.all().filter(
            is_published=True,
        )
        super_memory_serializer = Super_memorySerializer(
            super_memory,  many=True
        )
        return Response(super_memory_serializer.data)
