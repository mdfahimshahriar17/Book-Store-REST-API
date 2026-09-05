from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('register', views.RegistrationViewSet, basename='register')
urlpatterns = [
    path('',include(router.urls))
]