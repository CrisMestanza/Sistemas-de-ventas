from django.db import models
from software.models.CotizacionModel import Cotizacion


class CotizacionDetalle(models.Model):
    idcotizaciondetalle = models.AutoField(primary_key=True)
    idcotizacion = models.ForeignKey(Cotizacion, models.DO_NOTHING, db_column='idcotizacion', related_name='detalles')
    producto = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=500, blank=True, null=True)
    cantidad = models.FloatField()
    preciounitario = models.FloatField()
    subtotal = models.FloatField()

    class Meta:
        db_table = 'cotizacion_detalle'
