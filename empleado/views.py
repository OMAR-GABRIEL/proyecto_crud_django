from django.shortcuts import render,redirect
from .models import Empleado
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def home(request):
    listaempleados=Empleado.objects.all()
    return render(request,"home.html",{"empleados":listaempleados})
def insertempleado(request):
    codigo=request.POST['txtcodigo']
    nombre=request.POST['txtnombre']

    empleado=Empleado.objects.create(codigo=codigo,nombre=nombre)
    return redirect('/')

def borrarEmpleado(request,codigo):
    empleado=Empleado.objects.get(codigo=codigo)
    empleado.delete()
    return redirect('/')

def editEmpleado(request,codigo):
    empleado=Empleado.objects.get(codigo=codigo)
    return render(request, 'editEmpleado.html',{"empleado":empleado})

def modificar(request):
    if request.method == 'POST':
        codigo = request.POST['txtcodigo']
        

        try:
            empleado = Empleado.objects.get(codigo=codigo)
        except Empleado.DoesNotExist:
            return HttpResponse("Empleado no encontrado")
        empleado.nombre = request.POST['txtnombre']    
        empleado.save()
        return redirect('/')
        

            
            
            
                  
