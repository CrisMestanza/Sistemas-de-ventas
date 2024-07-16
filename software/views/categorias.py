from datetime import datetime, date
from decimal import Decimal
from django.db import connection
from software.views.apiBusquedaRUcDni import ApisNetPe
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
import templates
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
from software.models.TipoIgvModel import TipoIgv
from software.models.clientesModel import Clientes
# Create your views here.

def categorias(request):
    #Esto siempre va
    id2 = request.session.get('idtipousuario')
    if id2:
        permisos = Detalletipousuarioxmodulos.objects.filter(idtipousuario=id2)
        #Hata acá va 
        cateogiras_registros = Categoria.objects.filter(estado=1)
        
        data = {
            'cateogiras_registros':cateogiras_registros,
            "permisos":permisos #Esto se envía para mostrar los permisos
        }
        
        return render(request, 'categorias/categorias.html',data)
    else:
        return HttpResponse("<h1>No tiene acceso señor</h1>")
def eliminar(request, id):

    Categoria.objects.filter(idcategoria=id).update(estado=0)
    # Devuelve los datos JSON directamente sin redirigir
    return redirect('categorias')

def agregar(request):
    nombre = request.POST.get('nameCategoriaAgregar')
    Categoria.objects.create(nomcategoria=nombre,estado=1)
    return redirect('categorias')

def editar(request):
    id= request.POST.get('idCategoria')
    nombre= request.POST.get('nameCategoria')
    
    categoria = Categoria.objects.get(idcategoria=id)
    categoria.nomcategoria=nombre
    categoria.save()
    return redirect('categorias')
    