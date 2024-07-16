
from datetime import datetime
from decimal import Decimal
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from software.models.comprasModel import Compras
from software.models.ProveedoresModel import Proveedores
from software.models.TipoclienteModel import Tipocliente
from software.models.ProductoModel import Producto
from software.models.categoriaModel import Categoria
from software.models.compradetalleModel import CompraDetalle
from software.models.VentaModel import Venta
from software.models.VentaDetalleModel import VentaDetalle
from software.models.UsuarioModel import Usuario
from software.models.UnidadesModel import Unidades
from software.models.TipousuarioModel import Tipousuario
from software.models.TipodocumentoModel import Tipodocumento
from software.models.TipoclienteModel import Tipocliente
from software.models.ProvinciasModel import Provincias
from software.models.ProveedoresModel import Proveedores
from software.models.NumserieModel import Numserie
from software.models.ModulosModel import Modulos
from software.models.empresaModel import Empresa
from software.models.empleadoModel import Empleado
from software.models.distritosModel import Distritos
from software.models.detalletipousuarioxmodulosModel import Detalletipousuarioxmodulos
from software.models.detallecategoriaxunidadesModel import Detallecategoriaxunidades
from software.models.departamentosModel import Departamentos
from software.models.codigocorreoModel import CodigoCorreo
from software.models.clientesModel import Clientes
from django.db import connection
from openpyxl import Workbook
from openpyxl.utils import get_column_letter


def usuarios(request):
    id2 = request.session.get('idtipousuario')
    if id2:

        permisos = Detalletipousuarioxmodulos.objects.filter(idtipousuario=id2)
        usuarios = Usuario.objects.filter(estado=1)
        tipoUsuarios = Tipousuario.objects.filter(estado=1)
        data = {
            'usuarios': usuarios,
            'tipoUsuarios': tipoUsuarios,
            'permisos': permisos
        }
        return render(request, 'usuarios/usuarios.html', data)
    else:
        return HttpResponse("<h1>No tiene acceso señor</h1>")


def agregar(request):
    if request.method == "POST":
        try:
            nombreUsuario = request.POST.get('nombreUsuario2')
            correoUsuario = request.POST.get('correoUsuario2')
            contrasenaUsuario = request.POST.get('contrasenaUsuario2')
            tipoUsuario = request.POST.get('tipoUsuario2')
            celularUsuario = request.POST.get('celularUsuario2')
            dniUsuario = request.POST.get('dniUsuario2')

            # Traer la instancia de tipo usuario
            getTipoUsuario = get_object_or_404(
                Tipousuario, idtipousuario=tipoUsuario)

            usuario = Usuario.objects.create(
                nombrecompleto=nombreUsuario,
                correo=correoUsuario,
                contrasena=contrasenaUsuario,
                idtipousuario=getTipoUsuario,
                celular=celularUsuario,
                dni=dniUsuario,
                estado=1
            )
            usuario.save()
            return JsonResponse({"message": "Usuario agregado exitosamente"}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Método no permitido"}, status=405)


def editar(request):
    if request.method == "POST":
        try:
            idUsuario = request.POST.get('idusuario')
            nombreUsuario = request.POST.get('nombreUsuario')
            correoUsuario = request.POST.get('correoUsuario')
            contrasenaUsuario = request.POST.get('contrasenaUsuario')
            tipoUsuario = request.POST.get('tipoUsuario')
            celularUsuario = request.POST.get('celularUsuario')
            dniUsuario = request.POST.get('dniUsuario')

            # Traer la instancia de tipo usuario
            getTipoUsuario = get_object_or_404(
                Tipousuario, idtipousuario=tipoUsuario)

            usuario = get_object_or_404(Usuario, idusuario=idUsuario)
            usuario.nombrecompleto = nombreUsuario
            usuario.correo = correoUsuario
            usuario.contrasena = contrasenaUsuario
            usuario.idtipousuario = getTipoUsuario
            usuario.celular = celularUsuario
            usuario.dni = dniUsuario
            usuario.save()
            return JsonResponse({"message": "Usuario editado exitosamente"}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Método no permitido"}, status=405)


def eliminar(request, id):
    if request.method == "GET":
        try:
            usuario = get_object_or_404(Usuario, idusuario=id)
            usuario.estado = 0
            usuario.save()
            return JsonResponse({"message": "Usuario eliminado exitosamente"}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Método no permitido"}, status=405)
