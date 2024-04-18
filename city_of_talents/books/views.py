from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Book
from .serializer import BookSerializer


class books_list(APIView):
    def get(self, request):
        books = Book.objects.all().filter(is_published=True)

        books_serializer = BookSerializer(books, many=True, context={'request': request})
        return Response(books_serializer.data)


class books_detail(APIView):
    def get(self, request, books_id):
        book = get_object_or_404(Book.objects.all().filter(
            pk=books_id, is_published=True)
        )
        serializer = BookSerializer(book, context={'request': request})
        return Response(serializer.data)
