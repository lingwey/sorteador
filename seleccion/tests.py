from django.test import TestCase, Client
from django.urls import reverse
from participantes.models import Participante
from .models import Ganador

class SeleccionTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.p1 = Participante.objects.create(nombre="Anakin", apellido="Skywalker")
        self.p2 = Participante.objects.create(nombre="Obi-Wan", apellido="Kenobi")
        self.url = reverse('seleccion:sortear')

    def test_post_sortear_crea_ganador_y_redirige(self):
        """Verifica que al hacer POST se cree un registro de ganador y se redirija"""
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Ganador.objects.count(), 1)
        ultimo_ganador = Ganador.objects.first()
        self.assertIn(ultimo_ganador.participante, [self.p1, self.p2])

    def test_vista_muestra_ganador_por_url(self):
        """Verifica que si pasamos el ID por URL, la vista lo reconoce"""
        response = self.client.get(f"{self.url}?ganador_id={self.p1.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['ganador'], self.p1)
        self.assertContains(response, "Anakin")