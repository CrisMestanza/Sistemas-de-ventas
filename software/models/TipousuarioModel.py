from django.db import models

class Tipousuario(models.Model):
    idtipousuario = models.AutoField(primary_key=True)
    nombretipousuario = models.CharField(max_length=255)
    estado = models.IntegerField()
    es_superadmin = models.IntegerField(default=0)

    class Meta:
        managed = False
        db_table = 'tipousuario'