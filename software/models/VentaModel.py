from django.db import models

from software.models.NumserieModel import Numserie
from software.models.clientesModel import Clientes
from software.models.TipoIgvModel import TipoIgv
from software.models.empresaModel import Empresa
from software.models.ModopagoModel import Modopago


class Venta(models.Model):
    idventa = models.AutoField(primary_key=True)
    idnumserie = models.ForeignKey(
        Numserie, models.DO_NOTHING, db_column='idnumserie')
    numcorrelativo = models.CharField(max_length=10)
    idcliente = models.ForeignKey(
        Clientes, models.DO_NOTHING, db_column='idcliente')
    fechaemision = models.DateField()
    horaemision = models.TimeField()
    estado = models.IntegerField()
    ruta_pdf = models.CharField(max_length=500)
    ruta_ticket = models.CharField(max_length=500)
    ruta_cdr = models.CharField(max_length=500)
    respuesta_sunat_descripcion = models.CharField(max_length=500)
    respuesta_sunat_codigo = models.CharField(max_length=500)
    id_tipo_igv = models.ForeignKey(
        TipoIgv, models.DO_NOTHING, db_column='id_tipo_igv')
    idempresa = models.ForeignKey(
        Empresa, models.DO_NOTHING, db_column='idempresa')
    idmodoPago = models.ForeignKey(
        Modopago, models.DO_NOTHING, db_column='idmodoPago')

    total_gravada = models.DecimalField(max_digits=10, decimal_places=2)
    total_igv = models.DecimalField(max_digits=10, decimal_places=2)
    total_gratuita = models.DecimalField(max_digits=10, decimal_places=2)
    total_exonerada = models.DecimalField(max_digits=10, decimal_places=2)
    total_inafecta = models.DecimalField(max_digits=10, decimal_places=2)
    total_a_pagar = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'venta'
