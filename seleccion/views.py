from django.shortcuts import render
from django.utils import timezone
from participantes.models import Participante
import random
from .models import Ganador


def sortear (request):
    participantes = Participante.objects.all()
    ganador = None
    if request.method == 'POST':
       ganador = random.choice(list(participantes))
       Ganador.objects.create( participante=ganador, fecha_sorteo=timezone.now().date() )
    ganadores = Ganador.objects.all()
    return render(request, "base.html", {'participantes': participantes, 'ganador':ganador, 'ganadores':ganadores})
    
