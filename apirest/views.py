from django.shortcuts import render
from rest_framework import  viewsets
from .serializers import AsesorSerializer
from .models import Asesor

class AsesorViewSet (viewsets. ModelViewSet):
    queryset=Asesor.objects.all()
    serializer_class=AsesorSerializer
        
    
# Create your views here.
