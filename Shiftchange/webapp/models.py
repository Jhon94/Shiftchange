from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

from django.db.models.signals import pre_save
from django.dispatch import receiver


class Empleado(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    documento = models.IntegerField()
    correo = models.EmailField()
    activo = models.BooleanField()

    def __str__(self):
        return '{0} {1}'.format(self.nombre, self.apellido)


class Jornada(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Turno(models.Model):
    #tupla de dias laborales ChoiseField
    DIAS = (
        ('L','Lunes'),
        ('M', 'Martes'),
        ('MI', 'Miércoles'),
        ('J', 'Jueves'),
        ('V', 'Viernes'),
        ('S', 'Sábado'),
        ('D', 'Domingo')
    )
    jornada = models.ForeignKey(Jornada,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    dia_inicio = models.CharField(max_length=2, choices=DIAS, default='L')
    dia_fin = models.CharField(max_length=2, choices=DIAS, default='S')
    activo = models.BooleanField()
    empleados = models.ManyToManyField(Empleado,
                                       through='EmpTur',
                                       through_fields=('turno', 'empleado'))

    def __str__(self):
        return self.jornada.nombre


class EmpTur(models.Model):
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Empleado Turno'


class Funcion(models.Model):
    nombre = models.CharField(max_length=30)
    activo = models.BooleanField()
    empleados = models.ManyToManyField(Empleado,
                                       through='EmpFun',
                                       through_fields=('funcion', 'empleado'))
    # Cambia el nombre de los models dentro de el admin
    class Meta:
        verbose_name_plural = 'Funciónes'
    # Muestra el nombre de la funcion en la vista de admin
    def __str__(self):
        return self.nombre


class EmpFun(models.Model):
    funcion = models.ForeignKey(Funcion, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Empleado Función'
        verbose_name_plural = 'Empleado Función'
    #Esto sirve para que aparesca el nombre de empleado y funcion agregadas
    def __str__(self):
        return '{0} {1} : {2} '.format(self.empleado.nombre,
                                       self.empleado.apellido,
                                       self.funcion.nombre)


class Maquina(models.Model):
    tipo = models.ForeignKey(Funcion,
                             on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30, null=True, blank=True)
    activo = models.BooleanField()

    def __str__(self):
        return self.nombre


class TurnosGenerado(models.Model):
    funcion = models.ForeignKey(Funcion,
                                on_delete=models.CASCADE)
    maquina = models.ForeignKey(Maquina,
                                on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado,
                                 on_delete=models.CASCADE)
    turno = models.ForeignKey(Turno,
                              on_delete=models.CASCADE)
    dia_inicio = models.DateField()
    dia_fin = models.DateField()

    def __str__(self):
        return self.pk
