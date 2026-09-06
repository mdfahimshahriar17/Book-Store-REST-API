from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
# router.register('register', views.RegistrationView.as_view(), basename='register')
urlpatterns = [
    path('',include(router.urls)),
    path('register/', views.RegistrationView.as_view()),
]