from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

app_name = "participante"
router = DefaultRouter()
router.register( r'participantes', ParticipanteViewset, basename= 'participantes')

urlpatterns = [
    path("api/", include(router.urls) ),
]
