# Django
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Local
from .serializers import ProfesionSerializer
from .models import Profesion

class ProfesionView(APIView):
    def get(self, request):
        profesiones = Profesion.objects.all()
        serializer = ProfesionSerializer(profesiones, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProfesionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
