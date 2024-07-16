from datetime import datetime, date
from decimal import Decimal
from django.db import connection
from software.views.apiBusquedaRUcDni import ApisNetPe
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
import templates
from software.models.comprasModel import Compras
from collections import defaultdict
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
from software.models.TipoIgvModel import TipoIgv
from software.models.clientesModel import Clientes
# Create your views here.

def permisos(request):
    
    id2 = request.session.get('idtipousuario')
    if id2:

        permisos = Detalletipousuarioxmodulos.objects.filter(idtipousuario=id2)
        permisos2 = Detalletipousuarioxmodulos.objects.all()
        modulos = Modulos.objects.filter(estado=1)
        tipoUsuarios = Tipousuario.objects.filter(estado=1)
        permisos_por_tipo_usuario = defaultdict(list)
        
        for permiso in permisos2:
            permisos_por_tipo_usuario[permiso.idtipousuario.nombretipousuario].append(permiso)
            
        data = {
            'permisos_por_tipo_usuario': permisos_por_tipo_usuario.items(),
            'permisos':permisos,
            "modulos":modulos,
            "tipoUsuarios":tipoUsuarios
        }
        
        return render(request, 'permisos/permisos.html',data)
    else:
        return HttpResponse("<h1>No tiene acceso señor</h1>")

def agregaPermiso(request):
    idTipoUsuario2 = request.POST.get('tipoUsuario')
    permisos = request.POST.getlist("permisosTu[idmodulo][]")
    
    getTipoUsuarios = Tipousuario.objects.get(idtipousuario=idTipoUsuario2)
    
    for idPErmiso in permisos:
        
        modulo = Modulos.objects.get(idmodulo=idPErmiso)
        
        newPermiso = Detalletipousuarioxmodulos()
        newPermiso.idtipousuario = getTipoUsuarios
        newPermiso.idmodulo=modulo
        newPermiso.save()
    
    return redirect('permisos')

def eliminarPermiso(request,id):
    Detalletipousuarioxmodulos.objects.filter(idtipousuario=id).delete()
    return redirect('permisos')