
from django.shortcuts import render
from .models import Participante
from rest_framework import viewsets, permissions
from .serializers import ParticipanteSerializers  # nombre corregido


def base(request):
    return render(request, "base.html")

def mostrarparticipantes(request):
    participantes = Participante.objects.all()
    return render(request, 'participantes/participantes.html', {'participantes': participantes})

class ParticipanteViewset(viewsets.ModelViewSet):
    queryset = Participante.objects.all()
    serializer_class = ParticipanteSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    

    