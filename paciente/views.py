from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Paciente
from .serializers import PacienteSerializer
from rest_framework import status

# Dudas:
# 1-qué argumertos recibe get ? y por qué ?
# 2-cuando se ejecuta get_queryset?

class PacienteView(APIView):

    def get(self, request):

        pacientes = Paciente.objects.all()

        serializer = PacienteSerializer(pacientes, many=True)

        return Response({"success": True, "message": serializer.data})
    
    
    def post(self, request):

        dataSerializer = PacienteSerializer(data=request.data)

        if dataSerializer.is_valid():

            dataSerializer.save()
            return Response({"success": True, "message": "Paciente creado correctamente"})
        return Response(dataSerializer.errors, status=status.HTTP_400_BAD_REQUEST)