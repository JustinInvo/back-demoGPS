from django.contrib import admin
from carreras.models import Carrera

@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
    pass