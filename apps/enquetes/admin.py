# from django.contrib import admin

# from .models import Pergunta, Resposta

# class RespostaInline(admin.StackedInline):
#     model = Resposta
#     extra = 2

# class PerguntaAdmin(admin.ModelAdmin):
#     fields = ['data_pub', 'texto_da_pergunta']
#     inlines = [RespostaInline]

# admin.site.register(Pergunta, PerguntaAdmin)
# #admin.site.register(Resposta)

from django.contrib import admin
from .models import Reserva, Mesa, Horarios, Restaurantes, Usuarios

# Inline para Mesas em Restaurantes
class MesaInline(admin.TabularInline):
    model = Mesa
    extra = 1  # Número de campos extras a serem exibidos

# Admin personalizado para Restaurantes
class RestaurantesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'capacidadeDeMesas')  # Campos a serem exibidos na lista
    search_fields = ('nome',)  # Campo usado para busca
    inlines = [MesaInline]  # Exibe mesas relacionadas na página do restaurante

# Admin personalizado para Usuarios
class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone')  # Campos a serem exibidos na lista
    search_fields = ('nome', 'email')  # Campos usados para busca
    ordering = ('nome',)  # Ordena a lista pelo nome

# Admin personalizado para Mesa
class MesaAdmin(admin.ModelAdmin):
    list_display = ('numeroDaMesa', 'capacidadeDaMesa', 'restaurante')  # Campos a serem exibidos na lista
    search_fields = ('numeroDaMesa',)  # Campo usado para busca

# Admin personalizado para Reservas
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'restaurante', 'mesa', 'dataDaReserva', 'horaDaReserva', 'numero_de_pessoas')  # Campos a serem exibidos na lista
    search_fields = ('usuario__nome', 'restaurante__nome', 'mesa__numeroDaMesa')  # Campos usados para busca
    list_filter = ('dataDaReserva', 'restaurante')  # Filtros disponíveis na barra lateral
    ordering = ('-dataDaReserva', 'horaDaReserva')  # Ordena pela data da reserva (descendente) e hora
    autocomplete_fields = ['usuario', 'mesa', 'restaurante']  # Campos que suportam autocompletar
    fieldsets = (  # Agrupando campos em seções
        ('Informações da Reserva', {
            'fields': ('usuario', 'mesa', 'restaurante', 'numero_de_pessoas')
        }),
        ('Data e Hora', {
            'fields': ('dataDaReserva', 'horaDaReserva')
        }),
    )

# Registro dos modelos com suas classes Admin customizadas
admin.site.register(Reserva, ReservaAdmin)  # Reserva com o admin personalizado
admin.site.register(Mesa, MesaAdmin)  # Mesa com o admin personalizado
admin.site.register(Horarios)  # Horarios sem personalização
admin.site.register(Restaurantes, RestaurantesAdmin)  # Restaurantes com o admin personalizado
admin.site.register(Usuarios, UsuariosAdmin)  # Usuarios com o admin personalizado

