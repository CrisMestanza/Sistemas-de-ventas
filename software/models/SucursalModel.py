from django.db import models


class Sucursal(models.Model):
    idsucursal = models.AutoField(primary_key=True)
    nombre_sucursal = models.CharField(max_length=60, blank=True, null=True, db_column='nombre_sursal')

    class Meta:
        managed = False
        db_table = 'sucursal'
