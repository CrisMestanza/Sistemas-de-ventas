from django.db import models
from software.models.clientesModel import Clientes


class CuentaBancaria(models.Model):
    idcuentabancaria = models.AutoField(primary_key=True)
    idcliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='idcliente', related_name='cuentas')
    banco = models.CharField(max_length=50)
    numero_cuenta = models.CharField(max_length=50)
    tipo_cuenta = models.CharField(max_length=20, default='Ahorro')
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = 'cuenta_bancaria'
