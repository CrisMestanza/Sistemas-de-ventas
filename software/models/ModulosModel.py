from django.db import models


class Modulos(models.Model):
    idmodulo = models.AutoField(primary_key=True)
    nombremodulo = models.CharField(max_length=255)
    estado = models.IntegerField()
    url = models.CharField(max_length=45)
    logo = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'modulos'
