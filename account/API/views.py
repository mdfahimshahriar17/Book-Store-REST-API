from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from book import models
from . import serializer

class RegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        serializers = serializer.RegistrationSerializer(data = request.data)
        serializers.is_valid(raise_exception = True)
        user = serializers.save()

        token, crerated = Token.objects.get_or_create(user=user)
        return Response({
            'token' : token.key
        })


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response({'message' : "Logout successfully!!"})