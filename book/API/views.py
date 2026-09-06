from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
import django_filters.rest_framework

from book import models
from . import serializer
from . import pagination
class BookListViewSet(viewsets.ModelViewSet):
    #Bringing all the items from DB
    queryset = models.Book.objects.all()

    #Converting into Serializer
    serializer_class = serializer.BookListSerializer

    #Read Only For Unauthenticated user
    permission_classes = [IsAuthenticatedOrReadOnly]

    #filtering by author
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['author']

    #Searching by title
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title']

    #Ordering by price
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['price']

    #Pagination, How many item will be show in perpage
    pagination_class = pagination.BookPagination
