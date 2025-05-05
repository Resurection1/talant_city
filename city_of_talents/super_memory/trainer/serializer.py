from rest_framework import serializers
from .models import Trainer


class TrainerSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField('get_trainer')

    class Meta:
        model = Trainer
        fields = ['name', 'surname', 'description', 'photo']

    def get_trainer(self, trainer):
        request = self.context.get('request')
        if request and trainer.photo:
            return request.build_absolute_uri(trainer.photo.url)
        return None
