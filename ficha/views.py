# django
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# local
from .serializers import FichaSerializer
from .models import Ficha

class FichaView(APIView):

    def get(self, request): 
        fichas = Ficha.objects.all()
        fichasSerializer = FichaSerializer(fichas, many=True)
        return Response(fichasSerializer.data)

    def post(self, request):
        serializer = FichaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

