from django.db import models

from software.models.ProductoModel import Producto
from software.models.VentaModel import Venta

class VentaDetalle(models.Model):
    idventadetalle = models.AutoField(primary_key=True)
    idventa = models.ForeignKey(Venta, models.DO_NOTHING, db_column='idventa')
    idproducto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='idproducto')
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    preciosubtotal = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'venta_detalle'