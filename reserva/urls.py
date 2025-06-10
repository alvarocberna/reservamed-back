from django.urls import path
from .views import * 

urlpatterns = [
    path('reserva/', ReservaView.as_view(), name='reserva'),
]