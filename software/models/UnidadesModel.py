from django.db import models

class Unidades(models.Model):
    idunidad = models.AutoField(primary_key=True)
    codigounidad = models.CharField(max_length=255)
    abrunidad = models.CharField(max_length=255)
    estado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'unidades'