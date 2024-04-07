from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Book
from .serializer import BookSerializer


class books_list(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


class books_detail(APIView):
    def get(self, request, books_id):
        book = Book.objects.all().filter(pk=books_id)
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
