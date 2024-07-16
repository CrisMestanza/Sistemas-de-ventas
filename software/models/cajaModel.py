from django.db import models


class Caja(models.Model):
    id_caja = models.AutoField(primary_key=True)
    fecha_apertura = models.DateField(blank=True, null=True)
    hora_apertura = models.TimeField(blank=True, null=True)
    fecha_cierre = models.DateField(blank=True, null=True)
    hora_cierre = models.TimeField(blank=True, null=True)
    monto_inicial = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    monto_final = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    usuario_apertura = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_apertura', blank=True, null=True)
    usuario_cierre = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_cierre', related_name='caja_usuario_cierre_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'caja'

