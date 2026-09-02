from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from book import models
from . import serializer

class BookListViewSet(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializer.BookListSerializer

    def create(self, request, *args, **kwargs):
        serializers = self.get_serializer(data = request.data)
        serializers.is_valid(raise_exception = True)
        user = serializers.save()

        token, crerated = Token.objects.get_or_create(user=user)
        return Response({
            'token' : token.key
        })