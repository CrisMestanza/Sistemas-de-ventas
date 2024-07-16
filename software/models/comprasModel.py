from django.db import models
class Compras(models.Model):
    idcompra = models.AutoField(primary_key=True)
    idproveedor = models.ForeignKey('Proveedores', models.DO_NOTHING, db_column='idproveedor')
    numcorrelativo = models.CharField(max_length=11)
    fechacompra = models.DateField()
    estado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'compras'