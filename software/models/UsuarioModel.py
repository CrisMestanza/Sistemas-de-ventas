from django.db import models

from software.models.TipousuarioModel import Tipousuario

class Usuario(models.Model):
    idusuario = models.AutoField(primary_key=True)
    nombrecompleto = models.CharField(max_length=255)
    correo = models.CharField(max_length=255)
    contrasena = models.CharField(max_length=255)
    idtipousuario = models.ForeignKey(Tipousuario, models.DO_NOTHING, db_column='idtipousuario')
    celular = models.CharField(max_length=10)
    dni = models.CharField(max_length=10)
    estado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usuario'