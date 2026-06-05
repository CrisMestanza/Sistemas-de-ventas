from django.db import models
from software.models.SucursalModel import Sucursal

class Compras(models.Model):
    idcompra = models.AutoField(primary_key=True)
    idproveedor = models.ForeignKey('Proveedores', models.DO_NOTHING, db_column='idproveedor')
    numcorrelativo = models.CharField(max_length=50)
    fechacompra = models.DateField()
    estado = models.IntegerField()
    idsucursal = models.ForeignKey(Sucursal, models.DO_NOTHING, db_column='idsucursal', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compras'