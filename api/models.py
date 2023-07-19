from django.db import models
from django.db.models import CASCADE


class Author(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title



class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey("api.Author", null=True, on_delete=CASCADE)
    descriptions = models.CharField(max_length=255)

    def __str__(self):
        return self.title


models = [Author, Book]
