from django.shortcuts import render, redirect
from django.urls import reverse
from participantes.models import Participante
import random
from .models import Ganador


def sortear(request):
    participantes = Participante.objects.all()
    ganadores = Ganador.objects.all().order_by('-id')[:5]
    ganador = None
    ganador_id = request.GET.get('ganador_id')
    # Buscamos si viene un ganador_id por la URL (después del redirect)
    if ganador_id:
        ganador = Participante.objects.filter(id=ganador_id).first()

    if request.method == 'POST':
        # ... lógica de elección aleatoria ...
        nuevo = random.choice(list(participantes))
        Ganador.objects.create(participante=nuevo)
        # Redirigimos pasando el ID
        return redirect(f"{reverse('seleccion:sortear')}?ganador_id={nuevo.id}")            
    return render(request, "sorteo/sorteo.html", {
        'participantes': participantes, 
        'ganador': ganador, 
        'ganadores': ganadores
    })  
