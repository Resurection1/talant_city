from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Super_memory
from site_title.models import Trainer
from .serializer import Super_memorySerializer
from site_title.serializer import TrainerSerializer


class super_memory(APIView):
    def get(self, request):
        trainers = Trainer.objects.all().filter(
            is_published=True
        )
        super_memory = Super_memory.objects.all().filter(
            is_published=True,
        )
        super_memory_serializer = Super_memorySerializer(
            super_memory,  many=True
        )
        trainer_serializer = TrainerSerializer(trainers, many=True)

        data = {
            'curses': super_memory_serializer.data,
            'trainers': trainer_serializer.data
        }

        return Response(data)
