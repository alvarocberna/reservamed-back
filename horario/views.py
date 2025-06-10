# django
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# local
from .serializers import HorarioSerializer
from .models import Horario

class HorarioView(APIView):
    def get(self, request):
        horarios = Horario.objects.all()
        serializer = HorarioSerializer(horarios, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HorarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
