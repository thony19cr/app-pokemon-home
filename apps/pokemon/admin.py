from django.contrib import admin
from .models import Pokemon

# Register your models here.
#admin.site.register(Pokemon)


@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'generacion')
    list_filter = ('nombre', 'tipo')
    search_fields = ('nombre',)
    fields = ('nombre',)
