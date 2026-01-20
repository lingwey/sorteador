from django.shortcuts import render
from participantes.models import Participante
import random
from .models import Ganador


def sortear(request):
    participantes = Participante.objects.all()
    ganadores = Ganador.objects.all().order_by('-id')[:3]
    ganador = None

    if request.method == 'POST':
        if participantes.exists():
            ganador = random.choice(list(participantes))
            Ganador.objects.create(participante=ganador)
        
    return render(request, "sorteo/sorteo.html", {
        'participantes': participantes, 
        'ganador': ganador, 
        'ganadores': ganadores
    })  
