from django.db import models
class Distritos(models.Model):
    iddistrito = models.CharField(primary_key=True, max_length=11)
    nombredistrito = models.CharField(max_length=255)
    idprovincia = models.ForeignKey('Provincias', models.DO_NOTHING, db_column='idprovincia')
    ubigeo = models.CharField(max_length=255, blank=True, null=True)
    checked = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'distritos'