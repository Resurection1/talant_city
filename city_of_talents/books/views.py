from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Book
from .serializer import BookSerializer
from site_title.models import Trainer
from site_title.serializer import TrainerSerializer


class books_list(APIView):
    def get(self, request):
        books = Book.objects.all().filter(is_published=True)
        trainers = Trainer.objects.all().filter(is_published=True)

        booksserializer = BookSerializer(books, many=True)
        trainer_serializer = TrainerSerializer(trainers, many=True)

        data = {
            'books': booksserializer.data,
            'trainers': trainer_serializer.data
        }
        return Response(data)


class books_detail(APIView):
    def get(self, request, books_id):
        book = get_object_or_404(Book.objects.all().filter(
            pk=books_id, is_published=True)
        )
        serializer = BookSerializer(book)
        return Response(serializer.data)
