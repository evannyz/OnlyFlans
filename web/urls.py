from django.urls import path, include
from .views import vista_index, vista_about, vista_welcome, vista_contact, vista_exito, logouta, vista_cerrar_sesion, register, registro_con_exito
from . import views



urlpatterns = [
    path("", vista_index, name='indice'),
    path("acerca/", vista_about, name='acerca'),
    path("bienvenido/", vista_welcome, name='bienvenido'),
    path("contacto/", vista_contact, name="contacto"),
    path("exito/", vista_exito, name="exito"),
    path("accounts/", include('django.contrib.auth.urls')),
    path("cerrar_sesion/", vista_cerrar_sesion, name="cerrar_sesion"),
    path("logouta/", logouta, name="logouta"),
    path("registrar/", register, name="registrar"),
    path("registro_ex/", registro_con_exito, name="registro_ex"),
    path('flan/', views.flan_list, name='flan_list'),
    path('flan/create/', views.flan_create, name='flan_create'),
    path('flan/update/<uuid:pk>/', views.flan_update, name='flan_update'),
    path('flan/delete/<uuid:pk>/', views.flan_delete, name='flan_delete'),
    
]