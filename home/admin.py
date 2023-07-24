from django.contrib import admin
from home.models import Pesquisa

class PesquisaAdmin(admin.ModelAdmin):
    list_display = ('id','nome','eh_publicada')
    list_display_links = ('id','nome')
    search_fields = ('nome',)
    list_filter = ('categoria',)
    list_editable = ('eh_publicada',)
    list_per_page = 10

admin.site.register(Pesquisa,PesquisaAdmin)

