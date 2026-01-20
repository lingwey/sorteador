from rest_framework import serializers
from .models import Participante

class ParticipanteSerializers (serializers.ModelSerializer):
    class Meta:
        model= Participante
        fields = ['nombre', 'apellido'] 