from django.db import models

class Tipocliente(models.Model):
    idtipocliente = models.AutoField(primary_key=True)
    nomtipocliente = models.CharField(max_length=255)
    estado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipocliente'