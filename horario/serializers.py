from rest_framework import serializers
from .models import Horario

class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = '__all__'

    # ni idea que hace esto, lo tirò copilot, investigar 
    def create(self, validated_data):
        return Horario.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance