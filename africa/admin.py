from django.contrib import admin
from . import models

class Adm_Admin(admin.ModelAdmin):
    ...
admin.site.register(models.mod_africa,Adm_Admin)


 


