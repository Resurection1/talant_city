from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['title', 'author', 'publishing_house',
                  'the_year_of_publishing', 'ISBN',
                  'count_of_pages', 'format', 'circulation',
                  'link', 'photo']
