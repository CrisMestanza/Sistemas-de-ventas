from django.db import models

from software.models.categoriaModel import Categoria
from software.models.UnidadesModel import Unidades

class Producto(models.Model):
    idproducto = models.AutoField(primary_key=True)
    idcategoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='idcategoria')
    nomproducto = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    precioCompra = models.FloatField()
    preciounitario = models.FloatField()
    stockactual = models.IntegerField()
    imagenprod = models.CharField(max_length=255)
    estado = models.IntegerField()
    codigo = models.CharField(max_length=45)
    codigo_barras = models.CharField(max_length=45)
    idunidad = models.ForeignKey(Unidades, models.DO_NOTHING, db_column='idunidad')
    class Meta:
        managed = False
        db_table = 'producto'