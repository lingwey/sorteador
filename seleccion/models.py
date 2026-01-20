from django.db import models
from participantes.models import Participante

class Ganador(models.Model):
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE, related_name="ganadores")
    fecha_sorteo = models.DateField(auto_now_add= True)

    def __str__(self):
        return f"{self.participante.nombre} {self.participante.apellido} - {self.fecha_sorteo.strftime('%d/%m')}"

