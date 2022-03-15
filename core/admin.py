from django.contrib import admin
from core.models import Evento


class Evento_admin(admin.ModelAdmin):
    list_display = ('id','titulo', 'data_evento', 'data_criacao') # Quais os campos que eu quero que apareça na listagem
    list_filter = ('titulo', 'data_evento',) # Assim cria um filtro no site

admin.site.register(Evento, Evento_admin)
