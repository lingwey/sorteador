from django.urls import path
from . import views

app_name= "seleccion"

urlpatterns = [
    path("", views.sortear, name='sortear'),
]