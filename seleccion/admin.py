from django.contrib import admin
from .models import Ganador

@admin.register(Ganador)
class adminGanadores(admin.ModelAdmin):
    model = Ganador
