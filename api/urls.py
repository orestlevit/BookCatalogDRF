from django.urls import path

from .views import *

urlpatterns = [
    path('authors/', AuthorGetCreateView.as_view()),
    path('authors/<int:pk>/', AuthorDeleteUpdateView.as_view()),
    path('books/', BookGetCreateView.as_view()),
    path('books/<int:pk>/', BookDeleteUpdateView.as_view()),


]