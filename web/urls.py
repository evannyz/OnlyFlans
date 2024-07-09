from django.urls import path, include
from .views import vista_index, vista_about, vista_welcome, vista_contact, vista_exito, logouta, vista_cerrar_sesion, register, registro_con_exito
from . import views



urlpatterns = [
    # Ruta para la página de inicio
    path("", vista_index, name='indice'),

    # Ruta para la página "Acerca de"
    path("acerca/", vista_about, name='acerca'),

    # Ruta para la página de bienvenida (requiere autenticación de usuario)
    path("bienvenido/", vista_welcome, name='bienvenido'),

    # Ruta para la página de contacto
    path("contacto/", vista_contact, name="contacto"),

    # Ruta para la página de éxito después de enviar el formulario de contacto
    path("exito/", vista_exito, name="exito"),

    # Incluye las rutas de autenticación predeterminadas de Django
    path("accounts/", include('django.contrib.auth.urls')),

    # Ruta para mostrar la página de cierre de sesión
    path("cerrar_sesion/", vista_cerrar_sesion, name="cerrar_sesion"),

    # Ruta para cerrar la sesión del usuario
    path("logouta/", logouta, name="logouta"),

    # Ruta para la página de registro de usuarios
    path("registrar/", register, name="registrar"),

    # Ruta para la página de éxito después de registrar un usuario
    path("registro_ex/", registro_con_exito, name="registro_ex"),

    # Ruta para listar flanes (requiere ser miembro del staff)
    path('flan/', views.flan_list, name='flan_list'),

    # Ruta para crear un nuevo flan (requiere ser miembro del staff)
    path('flan/create/', views.flan_create, name='flan_create'),

    # Ruta para actualizar un flan existente (requiere ser miembro del staff)
    path('flan/update/<uuid:pk>/', views.flan_update, name='flan_update'),

    # Ruta para eliminar un flan (requiere ser miembro del staff)
    path('flan/delete/<uuid:pk>/', views.flan_delete, name='flan_delete'),
]