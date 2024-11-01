from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Isso liga a URL raiz à função home
    # Adicione mais padrões de URL conforme necessário
]
