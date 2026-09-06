from django.urls import path, include
from rest_framework.authtoken import views
from . import views as custom_views

urlpatterns = [


    path('login/', views.obtain_auth_token),

    path('register/', custom_views.RegistrationView.as_view()),
    path('logout/', custom_views.LogoutView.as_view()),
]