from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path ("", include("seleccion.urls", namespace='seleccion')),
    path("participantes/",include("participantes.urls", namespace='participantes')),
]
