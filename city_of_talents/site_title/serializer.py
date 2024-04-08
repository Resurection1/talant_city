from rest_framework import serializers
from .models import Curse, Location, Trainer


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['name']


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = ['name', 'surname', 'description']


class Site_titleSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    trainer = TrainerSerializer()

    class Meta:
        model = Curse
        fields = ['title', 'description', 'location',
                  'introductory_lecture',
                  'first_lesson', 'pub_date', 'trainer']
