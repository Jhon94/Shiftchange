from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib import admin
from webapp.views import (EmpleadoList,
                          InicioView,
                          UserUpdate,
                          ConsultaView,
                        #   EmpleadoAplicacionList,
                          FuncionAplicacionList,
                          MaquinaAplicacionList,
                          TurnoAplicacionList,
                          TurnoGeneradoAplicacionList,
                          TurnoCreation,
                          cambioEstado,
                          EmpleadoView

                          )

# from .views import *

urlpatterns = [

    path('inicio/', InicioView.as_view(), name='inicio'),
    path('empleados/', EmpleadoList.as_view(), name='empleado-list'),
    path('consulta/', ConsultaView.as_view(), name='consulta'),
    path('estado/<int:estado>/<int:usuario>/', cambioEstado,
         name='cambioEstado'),
    path('aplicacion_empleado/',EmpleadoView.as_view(),
         name='aplicacion_em'),
    path('aplicacion_funcion/', FuncionAplicacionList.as_view(),
         name='aplicacion_funcion'),
    path('aplicacion_maquina/', MaquinaAplicacionList.as_view(),
         name='aplicacion_maquina'),
    path('aplicacion_turno/', TurnoAplicacionList.as_view(),
         name='aplicacion_turno'),
    path('', TurnoCreation.as_view(template_name='aplicacion_turno'),
         name='aplicacion_turno'),
    path('aplicacion_rotaciones/', TurnoGeneradoAplicacionList.as_view(),
         name='aplicacion_rotaciones'),
    path('login/', auth_views.login,
         {'template_name': 'webapp/login_empresa.html'}, name='login'),
    path('logout/', auth_views.logout,
         {'next_page': 'login_empresa/'}, name='logout'),



    # path('login/', auth_views.LoginView.as_view(template_name='webapp/login_empresa.html')),
    # path('cambiar-clave/', auth_views.PasswordChangeView.as_view(template_name='cambiar_clave.html')),

    # path('inicio/', inicio, name='inicio'),
    # path('baseinicio/', BaseInicio.as_view(), name='base_inicio'),
    # path('registro/', registro, name='registro'),
    # path('cambiarclave/', cambiar_clave, name='cambiar-clave'),
    # path('base', base, name='base'),


    # url(r'^$', CourseList.as_view(), name='list'),
    # url(r'^(?P<pk>\d+)$', CourseDetail.as_view(), name='detail'),
    # url(r'^nuevo$', CourseCreation.as_view(), name='new'),
    # url(r'^editar/(?P<pk>\d+)$', CourseUpdate.as_view(), name='edit'),
    # url(r'^borrar/(?P<pk>\d+)$', CourseDelete.as_view(), name='delete'),

]
