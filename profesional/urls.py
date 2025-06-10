from django.urls import path
from .views import * 

urlpatterns = [
    path('profesion/', ProfesionalView.as_view(), name='profesional'),
]