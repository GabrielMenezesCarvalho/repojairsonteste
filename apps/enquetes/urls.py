from django.urls import path

from . import views

app_name = 'enquetes'

urlpatterns = [
    path('', views.nova_reserva, name='nova_reserva'),
    path('confirmacao/', views.confirmacao, name='confirmacao'),
]
