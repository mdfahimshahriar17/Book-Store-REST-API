from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from book import models
from . import serializer

class BookListViewSet(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializer.BookListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

