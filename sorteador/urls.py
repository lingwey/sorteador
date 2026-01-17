from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("participantes.urls", namespace='participantes')),
    path('api/', include('participantes.urls'))
]
