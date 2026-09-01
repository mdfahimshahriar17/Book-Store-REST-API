from rest_framework import serializers
from book import models

class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = '__all__'