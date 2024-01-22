"""
URL configuration for ultima project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from base.views import inicio, contato, reserva, agendamento, categoria, pet
from api.views import reservas, contatos, ReservaViewSet, ContatoViewSet, AgendamentoViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("api/reserva", ReservaViewSet )
router.register("api/contato", ContatoViewSet )
router.register("api/agendamento", AgendamentoViewSet )
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", inicio, name="inicio"),
    path("contato", contato, name="contato"),
    path("reserva", reserva, name="reserva"),
    path("agendamento", agendamento, name="agendamento"),
    path("categoria", categoria, name="categoria"),
    path("pet", pet, name="pet"),
    path("api/contatos", contatos, name="contatos"),
    path("api_auth/", include('rest_framework.urls')),
]
urlpatterns = urlpatterns + router.urls