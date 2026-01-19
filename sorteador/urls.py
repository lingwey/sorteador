from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("participantes/",include("participantes.urls", namespace='participantes')),
    path ("", include("seleccion.urls", namespace='seleccion')),
]
