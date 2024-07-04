from django.shortcuts import render, redirect
from .models import Flan
from .forms import  ContactFormModelForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Vista para la página de inicio
def vista_index(request):
    flanes = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {'flanes': flanes})

# Vista para la página "Acerca de"
def vista_about(request):
    return render(request, 'about.html')

# Vista para la página de bienvenida (requiere autenticación de usuario)
@login_required
def vista_welcome(request):
    flanes = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html', {'flanes': flanes})

# Vista para el formulario de contacto
def vista_contact(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exito')
    else:
        form = ContactFormModelForm()
    return render(request, 'contactus.html', {'form': form})

# Vista para la página de éxito después de enviar el formulario de contacto
def vista_exito(request):
    return render(request, 'success.html')

# Vista para el logout
def logouta(request):
    logout(request)
    return redirect('cerrar_sesion')

# Vista para mostrar la página de cierre de sesión
def vista_cerrar_sesion(request):
    return render(request, 'cerrar_sesion.html')

# Vista para el registro de usuarios
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("registro_ex")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/register.html", {"form": form})

# Vista para la página de éxito después de registrar un usuario
def registro_con_exito(request):
    return render(request, 'registro_exitoso.html')

