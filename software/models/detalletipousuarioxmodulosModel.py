from django.db import models
class Detalletipousuarioxmodulos(models.Model):
    iddetalletipousuarioxmodulos = models.AutoField(primary_key=True)
    idtipousuario = models.ForeignKey('Tipousuario', models.DO_NOTHING, db_column='idtipousuario')
    idmodulo = models.ForeignKey('Modulos', models.DO_NOTHING, db_column='idmodulo')

    class Meta:
        managed = False
        db_table = 'detalletipousuarioxmodulos'