from django.contrib import admin
from .models import Owner

# Register your models here.
# admin.site.register(Owner)


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais', 'edad')  #Configura los datos que se van a visulizar en la lista de registros en el admin
    search_fields = ('nombre', 'pais')         #Agrega un campo de búsqueda en la parte adminsitrativa
    fields = ('nombre', 'edad', 'pais', 'dni')                #Ocultar o visualizar los campos al momento de crear un registro
