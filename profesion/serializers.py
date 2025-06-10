from rest_framework import serializers
from .models import Profesion

class ProfesionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesion
        fields = '__all__'