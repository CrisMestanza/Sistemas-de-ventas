from django.db import models

class TipoIgv(models.Model):
    id_tipo_igv = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10)
    tipo_igv = models.CharField(max_length=60)
    codigo_de_tributo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipo_igvs'