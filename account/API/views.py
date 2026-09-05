from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from book import models
from django.contrib.auth.models import User
from . import serializer

class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializer.RegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializers = self.get_serializer(data = request.data)
        serializers.is_valid(raise_exception = True)
        user = serializers.save()

        token, crerated = Token.objects.get_or_create(user=user)
        return Response({
            'token' : token.key
        })