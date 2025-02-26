from django.contrib import admin
from .models import Gastronomia

# Register your models here.

class GastronomiaAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(Gastronomia, GastronomiaAdmin)