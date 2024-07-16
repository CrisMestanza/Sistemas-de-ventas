from django.db import models
from software.models.Tipo_entidadModel import TipoEntidad

class Clientes(models.Model):
    idcliente = models.AutoField(primary_key=True)
    idtipocliente = models.ForeignKey('Tipocliente', models.DO_NOTHING, db_column='idtipocliente')
    numdoc = models.CharField(max_length=25)
    razonsocial = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    estado = models.IntegerField()
    id_tipo_entidad = models.ForeignKey('TipoEntidad', models.DO_NOTHING, db_column='id_tipo_entidad')
    
    class Meta:
        managed = False
        db_table = 'clientes'