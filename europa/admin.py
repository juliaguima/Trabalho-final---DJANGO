from django.contrib import admin
from europa.models import Comentario
from . import models


class EuroAdmin(admin.ModelAdmin):
    ...
admin.site.register(models.model_europa,EuroAdmin)

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('id','coment','eh_publicada','usuario')
    list_display_links = ('id','coment')
    search_fields = ('coment',)
    list_filter = ('usuario',)
    list_editable = ('eh_publicada',)
    list_per_page = 10

admin.site.register(Comentario,ComentarioAdmin)








 


