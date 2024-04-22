from rest_framework import serializers
from .models import (Curse, Location,
                     Trainer, Timetable, Sign_up_for_a_course, Video, Reviews)
from django.core.validators import RegexValidator


class CurseSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField('get_photo')
    link_name = serializers.SerializerMethodField()

    class Meta:
        model = Curse
        fields = ['id', 'title', 'description_comment',
                  'description', 'photo', 'link_name']

    def get_photo(self, curse):
        request = self.context.get('request')
        if request and curse.photo:
            return request.build_absolute_uri(curse.photo.url)
        return None

    def get_link_name(self, obj):
        return [link.url for link in obj.link.all()]


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['name', 'address']


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = ['name', 'surname', 'description']


class TimetableSerializer(serializers.ModelSerializer):
    curse = CurseSerializer()
    location = LocationSerializer()
    trainer = TrainerSerializer()

    class Meta:
        model = Timetable
        fields = ['curse', 'location', 'trainer',
                  'introductory_lecture', 'first_lesson', 'pub_date']


class Sign_up_for_a_courseSerializer(serializers.ModelSerializer):
    phone_number_validator = RegexValidator(
        regex=r"^\d+$", message="Введите только цифры без лишних символов")

    class Meta:
        model = Sign_up_for_a_course
        fields = ['name', 'phone_number', 'email', 'curse', 'customer_comment']

    def validate_phone_number(self, value):
        self.phone_number_validator(value)
        return value

    def validate(self, attrs):
        return super().validate(attrs)


class VideoSerializer(serializers.ModelSerializer):
    link_name = serializers.SerializerMethodField()
    # file_link_names = serializers.SerializerMethodField(
    # 'get_file_link_names')

    class Meta:
        model = Video
        fields = ['title', 'description', 'link_name']

    def get_link_name(self, obj):
        return [link.url for link in obj.link.all()]

    # def get_file_link_names(self, obj):
    #     request = self.context.get('request')
    #     if request and obj.video_file.exists():
    #         file_urls = [request.build_absolute_uri(
    #             file_link.video_file.url) for file_link in obj.video_file.all()
    #         ]
    #         return file_urls
        # return None


class ReviewsSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField('get_photo')
    curse_name = serializers.SerializerMethodField()

    class Meta:
        model = Reviews
        fields = ['title', 'description', 'curse_name', 'photo']

    def get_photo(self, reviews):
        request = self.context.get('request')
        if request and reviews.photo:
            return request.build_absolute_uri(reviews.photo.url)
        return None

    def get_curse_name(self, obj):
        return obj.curse.title
