from dicionario.models import Palavra, Pagina, Configuracao
from django.contrib import admin


class PalavraAdmin(admin.ModelAdmin):
    search_fields = ('palavra', 'username')


admin.site.register(Palavra, PalavraAdmin)
admin.site.register(Pagina)
admin.site.register(Configuracao)
