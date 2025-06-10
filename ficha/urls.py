from django.urls import path
from .views import *

urlpatterns = [
    path('ficha/', FichaView.as_view(), name='ficha'),
]