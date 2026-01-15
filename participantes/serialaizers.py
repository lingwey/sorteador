from rest_framework import serializers
from .models import Participante

class ParticipanteSerializers (serializers.ModelSerializer):
    class META:
        model= Participante
        field = ['nombre', 'apellido'] 