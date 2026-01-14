from django.urls import path
from .views import prueba

app_name = "participante"

urlpatterns = [
    path("", prueba, name="prueba" )
]
