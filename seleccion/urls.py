from django.urls import path
from . import views

app_name= "sorteo"

urlpatterns = [
    path("", views.sortear, name='sortear'),
    path("sorteador/", views.sorteados, name='sorteados')
]