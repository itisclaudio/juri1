from django.contrib import admin
from .models import Area, Juez, Sala, Casacion


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']

@admin.register(Juez)
class JuezAdmin(admin.ModelAdmin):
    list_display = ['apellidos', 'nombres']

@admin.register(Casacion)
class CasacionAdmin(admin.ModelAdmin):
    list_display = ['numero', 'materia']