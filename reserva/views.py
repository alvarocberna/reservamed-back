# django
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# local
from .serializers import ReservaSerializer
from .models import Reserva

class ReservaView(APIView):
    def get(self, request):
        reservas = Reserva.objects.all()
        serializer = ReservaSerializer(reservas, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ReservaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
