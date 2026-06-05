from django.db import models

from software.models.SucursalModel import Sucursal


class Numserie(models.Model):
    idnumserie = models.AutoField(primary_key=True)
    idtipodocumento = models.ForeignKey('Tipodocumento', models.DO_NOTHING, db_column='idtipodocumento')
    idsucursal = models.ForeignKey(Sucursal, models.DO_NOTHING, db_column='idsucursal', blank=True, null=True)
    numserie = models.CharField(max_length=4, blank=True, null=True)
    estado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'numserie'