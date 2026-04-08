from django.shortcuts import redirect, render
from software.models.empresaModel import Empresa
from software.models.departamentosModel import Departamentos
from software.models.ProvinciasModel import Provincias
from software.models.distritosModel import Distritos
from django.http import HttpResponse, JsonResponse
from software.models.detalletipousuarioxmodulosModel import Detalletipousuarioxmodulos
import templates
import requests


def configuracion(request):

    id2 = request.session.get('idtipousuario')
    if id2:

        permisos = Detalletipousuarioxmodulos.objects.filter(idtipousuario=id2)
        empresa = Empresa.objects.all()
        departamentos = Departamentos.objects.all()
        modo = empresa[0].mododev
        data = {
            'empresas': empresa,
            'departamentos': departamentos,
            'modo': modo,
            'permisos': permisos
        }

        return render(request, 'configuracion/configuracion.html', data)
    else:
        return HttpResponse("<h1>No tiene acceso señor</h1>")


def buscarProvincias(request):
    id = request.GET.get('selected_value')
    provincias = Provincias.objects.filter(iddepartamento=id)

    provincias_list = list(provincias.values())
    return JsonResponse(provincias_list, safe=False)


def buscarDistritos(request):
    id = request.GET.get('selected_value')
    distritos = Distritos.objects.filter(idprovincia=id)

    distritos_list = list(distritos.values())
    return JsonResponse(distritos_list, safe=False)


def ubigueo(request):
    id = request.GET.get('selected_value')
    distritos = Distritos.objects.filter(iddistrito=id)

    distritos_list = list(distritos.values())
    return JsonResponse(distritos_list, safe=False)


def editarEmpresa(request):
    ruc = request.POST.get('ruc')
    razonSocial = request.POST.get('razonSocial')
    nombreComercia = request.POST.get('nombreComercia')
    Direccion = request.POST.get('Direccion')
    telefono = request.POST.get('telefono')
    user = request.POST.get('user')
    password = request.POST.get('password')
    ubigueo = request.POST.get('ubigueo')
    idempresaPost = request.POST.get('idempresa')

    # traer el distrito
    getDistrito = Distritos.objects.get(iddistrito=ubigueo)

    empresa = Empresa.objects.get(idempresa=idempresaPost)
    empresa.ruc = ruc
    empresa.razonsocial = razonSocial
    empresa.nombrecomercial = nombreComercia
    empresa.direccion = Direccion
    empresa.telefono = telefono
    empresa.passwordsec = password
    empresa.ubigueo = ubigueo
    empresa.iddistrito = getDistrito
    empresa.save()

    url = "http://127.0.0.1:8001/api/v1/companies"
    urlSucursal = "http://127.0.0.1:8001/api/v1/branches"

    print("Token en sesión antes de la solicitud API:", request.session.get(
        'api_token'))  # Debug: Verificar token antes de la solicitud

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {request.session.get('api_token')}"
    }

    body = {
        "ruc": ruc,
        "razon_social": razonSocial,
        "nombre_comercial": nombreComercia,
        "direccion": Direccion,
        "ubigeo": ubigueo,
        "distrito": getDistrito.nombredistrito,
        "provincia": getDistrito.idprovincia.nombreprovincia,
        "departamento": getDistrito.idprovincia.iddepartamento.nombredepartamento,
        "telefono": telefono,
        "email": "contacto@empresademo.com",
        "usuario_sol": "MODDATOS",
        "clave_sol": "MODDATOS",
        "modo_produccion": 0
    }

    bodySucursal = {
        "company_id": 1,
        "codigo": "0001",
        "nombre": nombreComercia,
        "direccion": Direccion,
        "ubigeo": ubigueo,
        "distrito": getDistrito.nombredistrito,
        "provincia": getDistrito.idprovincia.nombreprovincia,
        "departamento": getDistrito.idprovincia.iddepartamento.nombredepartamento,
        "telefono": telefono,
        "email": "principal@empresademo.com"
    }

    try:
        response = requests.post(url, json=body, headers=headers)
        data = response.json()

        print("Respuesta API Empresa:", data)

        responseSucursal = requests.post(
            urlSucursal, json=bodySucursal, headers=headers)
        dataSucursal = responseSucursal.json()

        print("Respuesta API Sucursal:", dataSucursal)

        return redirect('configuracion')

    except Exception as e:
                print("Error al consumir API:", str(e))



def agregarpem(request):
    if request.method == 'POST':

        idempresaPost = request.POST.get('idempresa')
        ruc = request.POST.get('ruc')
        razonSocial = request.POST.get('razonSocial')
        nombreComercia = request.POST.get('nombreComercia')
        Direccion = request.POST.get('Direccion')
        telefono = request.POST.get('telefono')
        password = request.POST.get('password')
        ubigueo = request.POST.get('ubigueo')

        certificado_password = request.POST.get('certificado_password')

        # archivos
        pem = request.FILES.get('pem')
        imagen = request.FILES.get('imagen')

        # DB LOCAL
        getDistrito = Distritos.objects.get(iddistrito=ubigueo)
        empresa = Empresa.objects.get(idempresa=idempresaPost)

        empresa.ruc = ruc
        empresa.razonsocial = razonSocial
        empresa.nombrecomercial = nombreComercia
        empresa.direccion = Direccion
        empresa.telefono = telefono
        empresa.passwordsec = password
        empresa.ubigueo = ubigueo
        empresa.iddistrito = getDistrito
        empresa.save()

        # 🔥 API DESTINO
        url = "http://127.0.0.1:8001/api/v1/companies/1"

        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {request.session.get('api_token')}"
        }

        # 🔥 FORM-DATA
        data = {
            "ruc": ruc,
            "razon_social": razonSocial,
            "nombre_comercial": nombreComercia,
            "direccion": Direccion,
            "ubigeo": ubigueo,
            "distrito": getDistrito.nombredistrito,
            "provincia": getDistrito.idprovincia.nombreprovincia,
            "departamento": getDistrito.idprovincia.iddepartamento.nombredepartamento,
            "telefono": telefono,
            "email": "empresademo@gmail.com",
            "usuario_sol": "MODDATOS",
            "clave_sol": "MODDATOS",
            "certificado_password": certificado_password,
            "modo_produccion": 0,
            "_method": "PUT"   # 🔥 IMPORTANTE
        }

        files = {}

        if pem:
            files["certificado_pem"] = (pem.name, pem, pem.content_type)

        if imagen:
            files["logo_path"] = (imagen.name, imagen, imagen.content_type)

        try:
            response = requests.post(url, data=data, files=files, headers=headers)

            print("STATUS:", response.status_code)
            print("RESPUESTA:", response.text)

            return redirect('configuracion')

        except Exception as e:
            print("ERROR:", str(e))
            return redirect('configuracion')



def produccion(request, id):
    empresa = Empresa.objects.get(idempresa=id)
    empresa.mododev = 1
    empresa.save()

    url = f"http://127.0.0.1:8001/api/v1/companies/{id}/activate"
    headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {request.session.get('api_token')}"
        }

    try:
        response = requests.post(url, headers=headers)
        data = response.json()

        print("Respuesta API Empresa:", data)

        return redirect('configuracion')

    except Exception as e:
            print("Error al consumir API:", str(e))
            
    return redirect('configuracion')


def desarrollo(request, id):
    empresa = Empresa.objects.get(idempresa=id)
    empresa.mododev = 0
    empresa.save()
    return redirect('configuracion')
