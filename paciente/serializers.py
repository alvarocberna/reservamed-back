from rest_framework import serializers
from .models import Paciente

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'  # Esto incluye todos los campos del modelo Paciente
        # Si quieres especificar campos específicos, puedes usar:
        # fields = ['id', 'nombre', 'edad', ...]
        # o excluir algunos campos con:
        # exclude = ['campo_a_excluir']