from django.db import models


class Modopago(models.Model):
    idmodoPago = models.AutoField(primary_key=True)
    modo_pago = models.CharField(max_length=45)
    
    class Meta:
        managed = False
        db_table = 'modopago'