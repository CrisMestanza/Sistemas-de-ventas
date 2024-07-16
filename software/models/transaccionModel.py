from django.db import models

class Transaccion(models.Model):
    id_transaccion = models.AutoField(primary_key=True)
    id_caja = models.ForeignKey('Caja', models.DO_NOTHING, db_column='id_caja', blank=True, null=True)
    id_tipo_transaccion = models.ForeignKey('TipoTransaccion', models.DO_NOTHING, db_column='id_tipo_transaccion', blank=True, null=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)
    descripcion= models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transaccion'