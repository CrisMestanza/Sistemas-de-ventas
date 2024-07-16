from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from software.models.comprasModel import Compras
from software.models.ProveedoresModel import Proveedores
from software.models.TipoclienteModel import Tipocliente
from software.models.compradetalleModel import CompraDetalle
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

import templates
# Create your views here.


def unidades(request):

    id2 = request.session.get('idtipousuario')
    if id2:

        permisos = Detalletipousuarioxmodulos.objects.filter(idtipousuario=id2)
        unidades = Unidades.objects.all()
        data = {
            'unidades': unidades,
            'permisos': permisos
        }
        return render(request, 'unidades/unidades.html', data)
    else:
        return HttpResponse("<h1>No tiene acceso señor</h1>")


def activo(request, id):
    unidades = Unidades.objects.get(idunidad=id)
    unidades.estado = 1
    unidades.save()
    return redirect('unidades')


def desactivo(request, id):
    unidades = Unidades.objects.get(idunidad=id)
    unidades.estado = 0
    unidades.save()
    return redirect('unidades')
