from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField('get_book')

    class Meta:
        model = Book
        fields = ['title', 'author', 'publishing_house',
                  'the_year_of_publishing', 'ISBN',
                  'count_of_pages', 'format', 'circulation',
                  'link', 'photo']

    def get_book(self, book):
        request = self.context.get('request')
        if request and book.photo:
            return request.build_absolute_uri(book.photo.url)
        return None
