# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Caja(models.Model):
    id_caja = models.AutoField(primary_key=True)
    fecha_apertura = models.DateField(blank=True, null=True)
    hora_apertura = models.TimeField(blank=True, null=True)
    fecha_cierre = models.DateField(blank=True, null=True)
    hora_cierre = models.TimeField(blank=True, null=True)
    monto_inicial = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    monto_final = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    usuario_apertura = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_apertura', blank=True, null=True)
    usuario_cierre = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_cierre', related_name='caja_usuario_cierre_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'caja'


class Categoria(models.Model):
    idcategoria = models.AutoField(primary_key=True)
    nomcategoria = models.CharField(max_length=255)
    estado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'categoria'


class Clientes(models.Model):
    idcliente = models.AutoField(primary_key=True)
    idtipocliente = models.IntegerField()
    numdoc = models.CharField(max_length=25, blank=True, null=True)
    razonsocial = models.CharField(max_length=255, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    id_tipo_entidad = models.ForeignKey('TipoEntidad', models.DO_NOTHING, db_column='id_tipo_entidad', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes'


class CodigoCorreo(models.Model):
    id_codigo_correo = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=45, blank=True, null=True)
    correo = models.CharField(max_length=80, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'codigo_correo'


class CompraDetalle(models.Model):
    idcompradetalle = models.AutoField(primary_key=True)
    idcompra = models.ForeignKey('Compras', models.DO_NOTHING, db_column='idcompra')
    idproducto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='idproducto')
    cantidad = models.IntegerField()
    subtotal = models.FloatField()

    class Meta:
        managed = False
        db_table = 'compra_detalle'


class Compras(models.Model):
    idcompra = models.AutoField(primary_key=True)
    idproveedor = models.ForeignKey('Proveedores', models.DO_NOTHING, db_column='idproveedor')
    numcorrelativo = models.CharField(max_length=11, blank=True, null=True)
    fechacompra = models.DateField(blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compras'


class Departamentos(models.Model):
    iddepartamentos = models.CharField(primary_key=True, max_length=11)
    nombredepartamento = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departamentos'


class Detallecategoriaxunidades(models.Model):
    iddetallecategoriaxunidades = models.AutoField(primary_key=True)
    idcategoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='idcategoria')
    idunidad = models.ForeignKey('Unidades', models.DO_NOTHING, db_column='idunidad')

    class Meta:
        managed = False
        db_table = 'detallecategoriaxunidades'


class Detalletipoigvxdepartamento(models.Model):
    iddetalletipoigvxdepartamento = models.AutoField(primary_key=True)
    id_tipo_igv = models.IntegerField()
    iddepartamentos = models.CharField(max_length=11, db_collation='latin1_swedish_ci', db_comment='\t')

    class Meta:
        managed = False
        db_table = 'detalletipoigvxdepartamento'


class Detalletipousuarioxmodulos(models.Model):
    iddetalletipousuarioxmodulos = models.AutoField(primary_key=True)
    idtipousuario = models.ForeignKey('Tipousuario', models.DO_NOTHING, db_column='idtipousuario')
    idmodulo = models.ForeignKey('Modulos', models.DO_NOTHING, db_column='idmodulo')

    class Meta:
        managed = False
        db_table = 'detalletipousuarioxmodulos'


class Distritos(models.Model):
    iddistrito = models.CharField(primary_key=True, max_length=11)
    nombredistrito = models.CharField(max_length=255)
    idprovincia = models.ForeignKey('Provincias', models.DO_NOTHING, db_column='idprovincia')
    ubigeo = models.CharField(max_length=255, blank=True, null=True)
    checked = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'distritos'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empleado(models.Model):
    empleado = models.OneToOneField('Empresa', models.DO_NOTHING, primary_key=True)
    idempresa = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=75, blank=True, null=True)
    telefono = models.CharField(max_length=9, blank=True, null=True)
    direccion = models.CharField(max_length=75, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado'


class Empresa(models.Model):
    idempresa = models.AutoField(primary_key=True)
    ruc = models.CharField(max_length=11)
    razonsocial = models.CharField(max_length=255)
    nombrecomercial = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    mododev = models.IntegerField()
    logo = models.CharField(max_length=255)
    telefono = models.CharField(max_length=25)
    usersec = models.CharField(max_length=255)
    passwordsec = models.CharField(max_length=255)
    ubigueo = models.CharField(max_length=10, blank=True, null=True)
    idsucursal = models.ForeignKey('Sucursal', models.DO_NOTHING, db_column='idsucursal', blank=True, null=True)
    iddistrito = models.ForeignKey(Distritos, models.DO_NOTHING, db_column='iddistrito', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresa'


class Lotes(models.Model):
    idlote = models.AutoField(db_column='idLote', primary_key=True)  # Field name made lowercase.
    idcompradetalle = models.ForeignKey(CompraDetalle, models.DO_NOTHING, db_column='idcompradetalle', blank=True, null=True)
    idproducto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='idproducto', blank=True, null=True)
    identificador = models.CharField(max_length=50)
    fecha_produccion = models.DateField(blank=True, null=True)
    fecha_vencimiento = models.DateField(blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lotes'


class Modopago(models.Model):
    idmodopago = models.AutoField(db_column='idmodoPago', primary_key=True)  # Field name made lowercase.
    modo_pago = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modopago'


class Modulos(models.Model):
    idmodulo = models.AutoField(primary_key=True)
    nombremodulo = models.CharField(max_length=255)
    estado = models.IntegerField()
    url = models.CharField(max_length=45, blank=True, null=True)
    logo = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modulos'


class Numserie(models.Model):
    idnumserie = models.AutoField(primary_key=True)
    idtipodocumento = models.ForeignKey('Tipodocumento', models.DO_NOTHING, db_column='idtipodocumento')
    numserie = models.CharField(max_length=4, blank=True, null=True)
    estado = models.IntegerField()
    idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='idusuario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'numserie'


class Producto(models.Model):
    idproducto = models.AutoField(primary_key=True)
    idcategoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='idcategoria', blank=True, null=True)
    nomproducto = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    preciocompra = models.FloatField(db_column='precioCompra', blank=True, null=True)  # Field name made lowercase.
    preciounitario = models.FloatField(blank=True, null=True)
    stockactual = models.IntegerField(blank=True, null=True)
    imagenprod = models.CharField(max_length=255, blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    codigo = models.CharField(max_length=45, blank=True, null=True)
    codigo_barras = models.CharField(max_length=45, blank=True, null=True)
    idunidad = models.ForeignKey('Unidades', models.DO_NOTHING, db_column='idunidad', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto'


class Proveedores(models.Model):
    idproveedor = models.AutoField(primary_key=True)
    idtipocliente = models.ForeignKey('Tipocliente', models.DO_NOTHING, db_column='idtipocliente')
    numdoc = models.CharField(max_length=255)
    razonsocial = models.CharField(max_length=255)
    estado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'proveedores'


class Provincias(models.Model):
    idprovincia = models.CharField(primary_key=True, max_length=11)
    nombreprovincia = models.CharField(max_length=255)
    iddepartamento = models.ForeignKey(Departamentos, models.DO_NOTHING, db_column='iddepartamento')

    class Meta:
        managed = False
        db_table = 'provincias'


class Sucursal(models.Model):
    idsucursal = models.IntegerField(primary_key=True)
    nombre_sursal = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sucursal'


class TipoEntidad(models.Model):
    id_tipo_entidad = models.AutoField(primary_key=True)
    tipo_entidad = models.CharField(max_length=45, blank=True, null=True)
    codigo = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    abreviatura = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_entidad'


class TipoIgvs(models.Model):
    id_tipo_igv = models.IntegerField(blank=True, null=True)
    codigo = models.IntegerField(blank=True, null=True)
    tipo_igv = models.CharField(max_length=255, blank=True, null=True)
    codigo_de_tributo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_igvs'


class TipoTransaccion(models.Model):
    id_tipo_transaccion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60, blank=True, null=True)
    ingresoegreso = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_transaccion'


class Tipocliente(models.Model):
    idtipocliente = models.AutoField(primary_key=True)
    nomtipocliente = models.CharField(max_length=255)
    estado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipocliente'


class Tipodocumento(models.Model):
    idtipodocumento = models.AutoField(primary_key=True)
    codigosunat = models.CharField(max_length=10)
    nombredocumento = models.CharField(max_length=255)
    abrrdoc = models.CharField(max_length=10)
    estado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipodocumento'


class Tipousuario(models.Model):
    idtipousuario = models.AutoField(primary_key=True)
    nombretipousuario = models.CharField(max_length=255)
    estado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipousuario'


class Transaccion(models.Model):
    id_transaccion = models.AutoField(primary_key=True)
    id_caja = models.ForeignKey(Caja, models.DO_NOTHING, db_column='id_caja', blank=True, null=True)
    id_tipo_transaccion = models.ForeignKey(TipoTransaccion, models.DO_NOTHING, db_column='id_tipo_transaccion', blank=True, null=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transaccion'


class Unidades(models.Model):
    idunidad = models.AutoField(primary_key=True)
    codigounidad = models.CharField(max_length=255)
    abrunidad = models.CharField(max_length=255)
    estado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'unidades'


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


class Venta(models.Model):
    idventa = models.AutoField(primary_key=True)
    idnumserie = models.ForeignKey(Numserie, models.DO_NOTHING, db_column='idnumserie')
    numcorrelativo = models.CharField(max_length=10, blank=True, null=True)
    idcliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='idcliente', blank=True, null=True)
    fechaemision = models.DateField(blank=True, null=True)
    horaemision = models.TimeField(blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    ruta_pdf = models.CharField(max_length=500, blank=True, null=True)
    ruta_cdr = models.CharField(max_length=500, blank=True, null=True)
    respuesta_sunat_descripcion = models.CharField(max_length=500, blank=True, null=True)
    respuesta_sunat_codigo = models.CharField(max_length=500, blank=True, null=True)
    id_tipo_igv = models.ForeignKey(TipoIgvs, models.DO_NOTHING, db_column='id_tipo_igv', blank=True, null=True)
    idempresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='idempresa', blank=True, null=True)
    idmodopago = models.ForeignKey(Modopago, models.DO_NOTHING, db_column='idmodoPago', blank=True, null=True)  # Field name made lowercase.
    total_gravada = models.FloatField(blank=True, null=True)
    total_igv = models.FloatField(blank=True, null=True)
    total_gratuita = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_exonerada = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_inafecta = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_a_pagar = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'venta'


class VentaDetalle(models.Model):
    idventadetalle = models.AutoField(primary_key=True)
    idventa = models.ForeignKey(Venta, models.DO_NOTHING, db_column='idventa')
    idproducto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='idproducto')
    cantidad = models.IntegerField()
    preciosubtotal = models.FloatField()

    class Meta:
        managed = False
        db_table = 'venta_detalle'
