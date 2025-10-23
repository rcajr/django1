from django.urls import path
from .views import organizador

urlpatterns = [
    path('organizador', organizador)
]