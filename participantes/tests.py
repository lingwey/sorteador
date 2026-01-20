from django.test import TestCase
from .models import Participante

class ParticipanteTest(TestCase):
    
    def setUp(self):
        #print("testeo de creacion")
        Participante.objects.create(nombre="Juan", apellido="Pérez")
        Participante.objects.create(nombre="Ana", apellido="García")

    def test_creacion_participante(self):
        #print("control de creacion")
        juan = Participante.objects.get(nombre="Juan")
        self.assertEqual(juan.apellido, "Pérez")

    def test_conteo_participantes(self):
        #print("test de canttidad")
        cantidad = Participante.objects.count()
        self.assertEqual(cantidad, 2)