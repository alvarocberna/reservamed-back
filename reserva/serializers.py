from rest_framework import serializers
from .models import Reserva

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'  
        # esto igual me lo tiro copilot, es interesante igual
        read_only_fields = ['id']  # El campo 'id' es de solo lectura