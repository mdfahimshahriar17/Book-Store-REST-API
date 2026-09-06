from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from . import views as custom_views

router = DefaultRouter()
# router.register('register', views.RegistrationView.as_view(), basename='register')
urlpatterns = [
    path('',include(router.urls)),
    path('login/', views.obtain_auth_token),
    path('register/', custom_views.RegistrationView.as_view()),
]