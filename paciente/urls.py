from django.urls import path
from .views import *

# dudas:
# 1-que argumentos recibe path ?
# 2-que significaba as_view() ?
# 3-para qué sirve el name ?

urlpatterns = [
    path('paciente/', PacienteView.as_view(), name='pacientes'),
]