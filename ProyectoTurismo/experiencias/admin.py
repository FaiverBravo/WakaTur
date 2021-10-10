from django.contrib import admin
from .models import Experiencia

# Register your models here.

class ExperienciaAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(Experiencia, ExperienciaAdmin)