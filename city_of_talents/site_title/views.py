from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Curse, Trainer
from .serializer import Site_titleSerializer, TrainerSerializer


class site_title(APIView):
    def get(self, request):
        trainers = Trainer.objects.all()

        curses = Curse.objects.select_related(
            'location', 'trainer'
        ).filter(
            is_published=True,
        ).order_by('-pub_date')

        curse_serializer = Site_titleSerializer(curses,  many=True)
        trainer_serializer = TrainerSerializer(trainers, many=True)

        data = {
            'curses': curse_serializer.data,
            'trainers': trainer_serializer.data
        }

        return Response(data)

        return Response(serializer.data)
