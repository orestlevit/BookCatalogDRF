import status
from django.shortcuts import render
from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework.views import APIView

from .models import Book, Author
from .serializer import BookSerializer, AuthorSerializer


class AuthorGetCreateView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get(self, requests):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, requests):
        obj = {
            "title": requests.data.get("title")
        }
        serializer = AuthorSerializer(data=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class AuthorDeleteUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get_object(self, author_id):
        try:
            return Author.objects.get(id=author_id)
        except Author.DoesNotExist:
            return None

    def delete(self, requests, pk):
        author_instance = self.get_object(pk)

        if author_instance is None:
            return Response({"response": "Task with this id does not exist"},
                            status.HTTP_404_NOT_FOUND)
        else:
            author_instance.delete()
            return Response({"response": "Author deleted"}, status.HTTP_200_OK)

    def patch(self, requests, pk):
        author_instance = self.get_object(pk)

        if author_instance is None:
            return Response({"response": "Task with this id does not exist"},
                            status.HTTP_404_NOT_FOUND)
        else:
            obj = {
                "title": requests.data.get("title")
            }
            serializer = AuthorSerializer(author_instance, data=obj)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class BookGetCreateView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get(self, requests):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, requests):
        serializer = BookSerializer(data=requests.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class BookDeleteUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get_object(self, book_id):
        try:
            return Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return None

    def delete(self, requests, pk):
        book_instance = self.get_object(pk)

        if book_instance is None:
            return Response({"response": "Task with this id does not exist"},
                            status.HTTP_404_NOT_FOUND)
        else:
            book_instance.delete()
            return Response({"response": "Book deleted"},
                            status.HTTP_200_OK)

    def patch(self, requests, pk):
        book_instance = self.get_object(pk)

        if book_instance is None:
            return Response({"response": "Task with this id does not exist"},
                            status.HTTP_404_NOT_FOUND)
        else:
            serializer = AuthorSerializer(book_instance, data=requests.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
