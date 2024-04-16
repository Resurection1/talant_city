from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Trainer
from .serializer import TrainerSerializer


class trainer_list(APIView):
    def get(self, request):
        trainers = Trainer.objects.all().filter(is_published=True)

        trainer_serializer = TrainerSerializer(trainers, many=True)
        return Response(trainer_serializer.data)
