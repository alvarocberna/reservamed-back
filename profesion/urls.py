from django.urls import path
from .views import *

urlpatterns = [
    path('profesion/', ProfesionView.as_view(), name='profesion'),
]