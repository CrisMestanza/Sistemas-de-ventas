from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from software.models.clientesModel import Clientes
from software.models.CuentaBancariaModel import CuentaBancaria
from software.models.detalletipousuarioxmodulosModel import Detalletipousuarioxmodulos

BANCOS = [
    'BCP', 'Interbank', 'BBVA', 'Scotiabank',
    'BanBif', 'Mibanco', 'Banco de la Nación',
    'Banco Pichincha', 'Banco Falabella', 'Yape / BCP', 'Plin',
]


def clientes_lista(request):
    id2 = request.session.get('idtipousuario')
    if not id2:
        return HttpResponse("<h1>No tiene acceso</h1>")
    permisos = Detalletipousuarioxmodulos.objects.filter(idtipousuario=id2)
    clientes = Clientes.objects.filter(estado=1).prefetch_related('cuentas').order_by('razonsocial')
    data = {'clientes': clientes, 'permisos': permisos, 'bancos': BANCOS}
    return render(request, 'clientes/clientes.html', data)


def cuentas_por_cliente(request):
    idcliente = request.GET.get('idcliente')
    if not idcliente:
        return JsonResponse([], safe=False)
    cuentas = CuentaBancaria.objects.filter(idcliente=idcliente, estado=1).values(
        'idcuentabancaria', 'banco', 'numero_cuenta', 'tipo_cuenta'
    )
    return JsonResponse(list(cuentas), safe=False)


def agregar_cuenta(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Método no permitido'}, status=405)
    try:
        idcliente = request.POST.get('idcliente')
        banco = request.POST.get('banco')
        numero_cuenta = request.POST.get('numero_cuenta', '').strip()
        tipo_cuenta = request.POST.get('tipo_cuenta', 'Ahorro')

        if not banco or not numero_cuenta:
            return JsonResponse({'error': 'Banco y número de cuenta son requeridos'}, status=400)

        cliente = get_object_or_404(Clientes, idcliente=idcliente)
        cuenta = CuentaBancaria.objects.create(
            idcliente=cliente,
            banco=banco,
            numero_cuenta=numero_cuenta,
            tipo_cuenta=tipo_cuenta,
            estado=1,
        )
        return JsonResponse({
            'success': True,
            'idcuentabancaria': cuenta.idcuentabancaria,
            'banco': cuenta.banco,
            'numero_cuenta': cuenta.numero_cuenta,
            'tipo_cuenta': cuenta.tipo_cuenta,
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


def eliminar_cuenta(request, id):
    CuentaBancaria.objects.filter(idcuentabancaria=id).update(estado=0)
    return JsonResponse({'success': True})
