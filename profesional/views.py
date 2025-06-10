# django
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# local
from .serializers import ProfesionalSerializer
from .models import Profesional

class ProfesionalView(APIView):
    def get(self, request):
        profesionales = Profesional.objects.all()
        serializer = ProfesionalSerializer(profesionales, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProfesionalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

