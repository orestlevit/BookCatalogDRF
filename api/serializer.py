from rest_framework import serializers
from .models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


        def create(self, requests):
            Book.objects.create({
                "title": requests.data.get("title"),
                "author": requests.author.id,
                "description": requests.data.get("description")
            })