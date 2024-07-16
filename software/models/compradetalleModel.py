from django.db import models

class CompraDetalle(models.Model):
    idcompradetalle = models.AutoField(primary_key=True)
    idcompra = models.ForeignKey('Compras', models.DO_NOTHING, db_column='idcompra')
    idproducto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='idproducto')
    cantidad = models.IntegerField()
    subtotal = models.FloatField()

    class Meta:
        managed = False
        db_table = 'compra_detalle'