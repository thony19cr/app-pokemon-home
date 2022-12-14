from django.db import models


class Catalog(models.Model):
    nombre_catalogo = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=120)
