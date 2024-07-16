from django.db import models

class CodigoCorreo(models.Model):
    id_codigo_correo = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=45, blank=True, null=True)
    correo = models.CharField(max_length=80, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'codigo_correo'