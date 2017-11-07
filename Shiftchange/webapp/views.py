from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.views import View
from django.http import HttpResponse

from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import *



class EmpleadoView(View):

    def get(self, request, *args, **kwargs):
        empleado = Empleado.objects.all()
        return render(request, 'webapp/aplicacion_empleado.html', {'empleado': empleado})

    def post(self, request, *args, **kwargs):
        print(request.POST['nombre'])
        print(request.POST['apellido'])
        print(request.POST['documento'])
        print(request.POST['correo'])
        print(request.POST['activo'])
        empleado = Empleado(nombre=request.POST['nombre'],
                    apellido=request.POST['apellido'],
                    documento=request.POST['documento'],
                    correo=request.POST['correo'],
                    estado=request.POST['estado'])
        empleado.save()
        return HttpResponse('Ok')


def cambioEstado(request, estado, usuario):
    empleado = Empleado.objects.get(pk=nombre)
    if estado:
        empleado.is_active = 1
    else:
        empleado.is_active = 0
    empleado.save()
    return HttpResponse(empleado)


class ConsultaView(TemplateView):

    template_name = "webapp/consulta_empleado.html"

    def get_context_data(self, **kwargs):
        ctx = super(ConsultaView, self).get_context_data(**kwargs)
        ctx['models'] = Empleado.objects.all()
        return ctx


class InicioView(TemplateView):
    template_name = "webapp/inicio.html"


#CRUD USER
class UserDetail(DetailView):
    model = User


class UserCreation(CreateView):
    model = User
    success_url = reverse_lazy('webapp:list')
    fields = ["username", "password", "first_name", "last_name", "is_active"]


class UserUpdate(UpdateView):
    model = User
    success_url = reverse_lazy('webapp:list')
    fields = ["username", "password", "first_name", "last_name", "is_active"]


class UserDelete(DeleteView):
    model = User
    success_url = reverse_lazy('webapp:list')


# CRUD FUNCION
class FuncionAplicacionList(ListView):
    model = Funcion
    template_name = "webapp/aplicacion_funcion.html"



# CRUD MAQUINA
class MaquinaAplicacionList(ListView):
    model = Maquina
    template_name = "webapp/aplicacion_maquina.html"


# CRUD EMPLEADO
class EmpleadoAplicacionList(ListView):
    model = Empleado
    template_name = "webapp/aplicacion_empleado.html"




# CRUD TURNO
class TurnoAplicacionList(ListView):
    model = Turno
    template_name = "webapp/aplicacion_turno.html"


class TurnoGeneradoAplicacionList(ListView):
    model = TurnosGenerado
    template_name = "webapp/aplicacion_rotaciones.html"


class EmpleadoList(ListView):
    model = Empleado


class EmpleadoDetail(DetailView):
    model = Empleado



class EmpleadoCreation(CreateView):
    model = Empleado
    success_url = reverse_lazy('webapp:list')
    fields = ["nombre", "apellido", "documento", "correo", "activo"]


class EmpleadoUpdate(UpdateView):
    model = Empleado
    success_url = reverse_lazy('webapp:list')
    fields = ["nombre", "apellido", "documento", "correo", "activo"]


class EmpleadoDelete(DeleteView):
    model = Empleado
    success_url = reverse_lazy('webapp:list')

# FIN CRUD EMPLEADO

# CRUD JORNADA
class JornadaList(ListView):
    model = Jornada


class JornadaDetail(DetailView):
    model = Jornada


class JornadaCreation(CreateView):
    model = Jornada
    success_url = reverse_lazy('webapp:list')
    fields = ["nombre"]


class JornadaUpdate(UpdateView):
    model = Jornada
    success_url = reverse_lazy('webapp:list')
    fields = ["nombre"]


class JornadaDelete(DeleteView):
    model = Jornada
    success_url = reverse_lazy('webapp:list')

#FIN CRUD JORNADA

class TurnoList(ListView):
    model = Turno


class TurnoDetail(DetailView):
    model = Turno


class TurnoCreation(CreateView):
    model = Turno
    success_url = reverse_lazy('webapp:list')
    fields = ["jornada","hora_inicio","hora_fin","dia_inicio","dia_fin","activo","empleados"]


class TurnoUpdate(UpdateView):
    model = Turno
    success_url = reverse_lazy('webapp:list')
    fields = ["jornada","hora_inicio","hora_fin","dia_inicio","dia_fin","activo","empleados"]


class TurnoDelete(DeleteView):
    model = Turno
    success_url = reverse_lazy('webapp:list')

#FIN CRUD Turno
#INICIO CRUD EmpTur

class EmpTurList(ListView):
    model = EmpTur


class EmpTurDetail(DetailView):
    model = EmpTur


class EmpTurCreation(CreateView):
    model = EmpTur
    success_url = reverse_lazy('webapp:list')
    fields = ["turno","empleado"]


class EmpTurUpdate(UpdateView):
    model = EmpTur
    success_url = reverse_lazy('webapp:list')
    fields = ["turno","empleado"]


class EmpTurDelete(DeleteView):
    model = EmpTur
    success_url = reverse_lazy('webapp:list')

#FIN EmpTur
#INICIO CRUD Funcion

class FuncionList(ListView):
    model = Funcion


class FuncionDetail(DetailView):
    model = Funcion


class FuncionCreation(CreateView):
    model = Funcion
    success_url = reverse_lazy('webapp:list')
    fields = ["nombre","activo","empleados"]


class FuncionUpdate(UpdateView):
    model = Funcion
    success_url = reverse_lazy('webapp:list')
    fields = ["nombre","activo","empleados"]


class FuncionDelete(DeleteView):
    model = Funcion
    success_url = reverse_lazy('webapp:list')

# FIN CRUD FUNCION
#INICIO CRUD EmpFun

class EmpFunList(ListView):
    model = EmpFun


class EmpFunDetail(DetailView):
    model = EmpFun


class EmpFunCreation(CreateView):
    model = EmpFun
    success_url = reverse_lazy('webapp:list')
    fields = ["funcion","empleado"]


class EmpFunUpdate(UpdateView):
    model = EmpFun
    success_url = reverse_lazy('webapp:list')
    fields = ["funcion","empleado"]


class EmpFunDelete(DeleteView):
    model = EmpFun
    success_url = reverse_lazy('webapp:list')

#FIN CRUD EmpFun
#INICIO CRUD Maquina

class MaquinaList(ListView):
    model = Maquina


class MaquinaDetail(DetailView):
    model = Maquina


class MaquinaCreation(CreateView):
    model = Maquina
    success_url = reverse_lazy('webapp:list')
    fields = ["tipo","nombre","activo"]


class MaquinaUpdate(UpdateView):
    model = Maquina
    success_url = reverse_lazy('webapp:list')
    fields = ["tipo","nombre","activo"]


class MaquinaDelete(DeleteView):
    model = Maquina
    success_url = reverse_lazy('webapp:list')

# FIN CRUD Maquina
# INICIO CRUD TurnosGenerado

class TurnosGeneradoList(ListView):
    model = TurnosGenerado


class TurnosGeneradoDetail(DetailView):
    model = TurnosGenerado


class TurnosGeneradoCreation(CreateView):
    model = TurnosGenerado
    success_url = reverse_lazy('webapp:list')
    fields = ["funcion","maquina","empleado","turno","dia_inicio","dia_fin"]


class TurnosGeneradoUpdate(UpdateView):
    model = Maquina
    success_url = reverse_lazy('webapp:list')
    fields = ["funcion","maquina","empleado","turno","dia_inicio","dia_fin"]


class TurnosGeneradoDelete(DeleteView):
    model = TurnosGenerado
    success_url = reverse_lazy('webapp:list')

#FIN CRUD TurnosGenerado
