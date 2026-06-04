from django.db import models
from software.models.clientesModel import Clientes


class Cotizacion(models.Model):
    idcotizacion = models.AutoField(primary_key=True)
    idcliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='idcliente', related_name='cotizaciones')
    fecha = models.DateField(auto_now_add=True)
    total = models.FloatField(default=0)
    observaciones = models.CharField(max_length=500, blank=True, null=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = 'cotizacion'
