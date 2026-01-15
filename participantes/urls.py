from django.urls import path
from . import views

app_name = "participante"

urlpatterns = [
    path("", views.prueba, name="prueba" )
]
