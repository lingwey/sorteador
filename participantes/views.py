from django.shortcuts import render
from .models import Participante
from rest_framework import viewsets
from .serialaizers import ParticipanteSerializers

def prueba(request):
    return render (request,"participantes/participantes.html")

class ParticipanteViewset():
    queryset= Participante.objects.all()
    serialaizer_class= ParticipanteSerializers
    

    