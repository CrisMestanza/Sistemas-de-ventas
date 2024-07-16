from django.db import models

from software.models.departamentosModel import Departamentos

class Provincias(models.Model):
    idprovincia = models.CharField(primary_key=True, max_length=11)
    nombreprovincia = models.CharField(max_length=255)
    iddepartamento = models.ForeignKey(Departamentos, models.DO_NOTHING, db_column='iddepartamento')

    class Meta:
        managed = False
        db_table = 'provincias'