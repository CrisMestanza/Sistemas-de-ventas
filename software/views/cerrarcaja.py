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
from software.models.cajaModel import Caja
from software.models.transaccionModel import Transaccion
from software.models.tipoTransaccion import TipoTransaccion
from django.utils import timezone

def cerrarcaja(request):
    #Esto siempre va
    id2 = request.session.get('idtipousuario')
    if id2:
        permisos = Detalletipousuarioxmodulos.objects.filter(idtipousuario=id2)
        
        # Obtener la fecha y hora actual en el huso horario de Lima (Perú)
        ahora = timezone.localtime(timezone.now())

        transacciones = Transaccion.objects.filter(fecha = ahora.date())
        
        suma = 0
        resta = 0
        for transaccion in transacciones:
            estado = transaccion.id_tipo_transaccion.ingresoegreso
            
            if estado == 1:
                suma += transaccion.monto
            elif estado == 0:
                resta += transaccion.monto
        total = suma-resta
        
        data = {

            "permisos":permisos, #Esto se envía para mostrar los permisos
            "total":total
        }
        
        return render(request, 'caja/cerrarCaja.html',data)
    else:
        return HttpResponse("<h1>No tiene acceso señor</h1>")
    
def finalizarCaja(request):
    monto_str = request.POST.get('monto')
    montoFinal = monto_str.replace(',', '.')
    
    usuario = Usuario.objects.get(idusuario=request.session.get('idusuario'))
    
    # Obtener la fecha y hora actual en el huso horario de Lima (Perú)
    ahora = timezone.localtime(timezone.now())
    
    ultimo_registro = Caja.objects.order_by('-id_caja').first()
    ultimo_registro.fecha_cierre = ahora.date()
    ultimo_registro.hora_cierre = ahora.time()
    ultimo_registro.monto_final = montoFinal
    ultimo_registro.usuario_cierre = usuario
    ultimo_registro.estado = 0
    ultimo_registro.save()
    return HttpResponse('La caja ha sido cerrada exitosamente.')