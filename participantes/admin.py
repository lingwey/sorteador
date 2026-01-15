from django.contrib import admin
from .models import Participante 

@admin.register(Participante)
class ParticipanteAdmin (admin.ModelAdmin):
    model = Participante
