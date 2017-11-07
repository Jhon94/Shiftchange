# from django import forms
# from .models import *
#
# class Empleadoform(forms.ModelForm):
#     class Meta:
#         model = Empleado
#         fields = ["nombre", "apellido", "documento", "correo", "activo"]
#
#
# class Jornadaform(forms.ModelForm):
#     class Meta:
#         model = Jornada
#         fields = ["nombre"]
#
#
# class Turnoform(forms.ModelForm):
#     class Meta:
#         model = Turno
#         fields = ["jornada","hora_inicio","hora_fin","dia_inicio","dia_fin","activo","empleados"]
#
#
# class EmpTurform(forms.ModelForm):
#     class Meta:
#         model = EmpTur
#         fields = ["turno","empleado"]
#
#
# class Funcionform(forms.ModelForm):
#     class Meta:
#         model = Funcion
#         fields = ["nombre","activo","empleados"]
#
#
# class EmpFunform(forms.ModelForm):
#     class Meta:
#         model = EmpFun
#         fields = ["funcion","empleado"]
#
#
# class Maquinaform(forms.ModelForm):
#     class Meta:
#         model = Maquina
#         fields = ["tipo","nombre","activo"]
#
#
# class TurnosGeneradoform(forms.ModelForm):
#     class Meta:
#         model = TurnosGenerado
#         fields = ["funcion","maquina","empleado","turno","dia_inicio","dia_fin"]
