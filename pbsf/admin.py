from django.contrib import admin
from .models import Vacina

@admin.register(Vacina)
class VacinaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'publico_alvo']
    list_filter = ['publico_alvo']
    search_fields = ['nome']
