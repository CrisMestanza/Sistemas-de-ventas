from django.db import models

class TipoEntidad(models.Model):
    id_tipo_entidad = models.AutoField(primary_key=True)
    tipo_entidad = models.CharField(max_length=45, blank=True, null=True)
    codigo = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    abreviatura = models.CharField(max_length=45, blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'tipo_entidad'