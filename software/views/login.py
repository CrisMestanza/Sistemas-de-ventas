from django.shortcuts import redirect, render
import templates 

from software.models.UsuarioModel import Usuario
from software.models.cajaModel import Caja
from software.models.TipousuarioModel import Tipousuario
from software.models.ModulosModel import Modulos
from software.models.detalletipousuarioxmodulosModel import Detalletipousuarioxmodulos
from django.utils import timezone
# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    email= request.POST['email_1']
    contrasena2 = request.POST['contrasena']
    if email and contrasena2:
         
        usuarios = Usuario.objects.filter(contrasena=contrasena2, correo=email).first()

        if usuarios:
            request.session['idtipousuario'] = usuarios.idtipousuario.idtipousuario
            request.session['nombrecompleto'] = usuarios.nombrecompleto
            request.session['idusuario'] = usuarios.idusuario
            
            ultimo_registro = Caja.objects.order_by('-id_caja').first()
            if ultimo_registro.estado ==1:
             
                return redirect('cpanel')
            else:
              
                return render(request,'caja/caja.html')
  
        else:
            error = "Correo o contraseña incorrecta"
            
            data = {
                "error": error,
            }
            return render(request, 'index.html',data)
    else:
        return HttpResponse("<h1>No tiene accedo señor</h1>")
    
    

def logout(request):
    # Eliminar la sesión completa
    request.session.flush()
    
    return redirect('index')  # Asegúrate de que 'index' sea el nombre correcto de la ruta hacia tu página inicial
  


#Para caja 
def caja(request):
    monto = request.POST.get('monto')
    
    # Obtener el usuario actual desde la sesión
    usuario = Usuario.objects.get(idusuario=request.session.get('idusuario'))

    # Obtener la fecha y hora actual en el huso horario de Lima (Perú)
    ahora = timezone.localtime(timezone.now())

    caja = Caja()
    caja.fecha_apertura = ahora.date()
    caja.hora_apertura = ahora.time()
    caja.monto_inicial = monto
    caja.usuario_apertura = usuario
    caja.estado = 1 #1 Apertura 0 cierre 
    caja.save()
    
    return redirect('cpanel')
        
