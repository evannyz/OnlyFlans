from django.shortcuts import render, redirect, get_object_or_404
from .models import Flan
from .forms import  ContactFormModelForm, CustomUserCreationForm, FlanForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.admin.views.decorators import staff_member_required


# Vista para la página de inicio
def vista_index(request):
    # Filtra los flanes que no son privados y los pasa al template
    flanes = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {'flanes': flanes})

# Vista para la página "Acerca"
def vista_about(request):
    return render(request, 'about.html')

# Vista para la página de bienvenida (requiere autenticación de usuario)
@login_required
def vista_welcome(request):
    # Filtra los flanes privados y los pasa al template
    flanes = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html', {'flanes': flanes})

# Vista para el formulario de contacto (vista común)
def vista_contact(request):
    if request.method == 'POST': # Si el formulario ha sido enviado
        form = ContactFormModelForm(request.POST) # Llena el formulario con los datos enviados
        if form.is_valid(): # Verifica si el formulario es válido
            form.save() # Guarda el formulario en la base de datos
            return redirect('exito')  # Redirige a la página de éxito
    else:
        form = ContactFormModelForm() # En el caso de no realizar un post genera un get o alguna otra respuesta, Crea un formulario vacío
    return render(request, 'contactus.html', {'form': form})

# Vista para la página de éxito después de enviar el formulario de contacto
def vista_exito(request):
    return render(request, 'success.html')

# Vista para el logout (alternativa a cierre de sesion de django)
def logouta(request):
    logout(request)
    return redirect('cerrar_sesion')

# Vista para mostrar la página de cierre de sesión
def vista_cerrar_sesion(request):
    return render(request, 'cerrar_sesion.html')

# Vista para el registro de usuarios
def register(request):
    if request.method == "POST":  # Si el formulario ha sido enviado desde el html
        form = CustomUserCreationForm(request.POST) # Llena el formulario con los datos enviados
        if form.is_valid(): # Verifica si el formulario es válido
            form.save() # Guarda el nuevo usuario en la base de datos
            return redirect("registro_ex") # Redirige a la página de éxito
    else:
        form = CustomUserCreationForm()  # Crea un formulario vacío
    return render(request, "registration/register.html", {"form": form})  # Renderiza el template con el formulario

# Vista para la página de éxito después de registrar un usuario
def registro_con_exito(request):
    return render(request, 'registro_exitoso.html')

@staff_member_required
def flan_list(request):
    # Obtiene todos los flanes y los pasa al template
    flanes = Flan.objects.all()
    return render(request, 'flan_list.html', {'flanes': flanes})

# Vista para crear un nuevo flan (requiere ser miembro del staff)
@staff_member_required
def flan_create(request):
    if request.method == 'POST': # Si el formulario ha sido enviado
        form = FlanForm(request.POST) # Llena el formulario con los datos enviados
        if form.is_valid():  # Verifica si el formulario es válido
            form.save() # Guarda el nuevo flan en la base de datos
            return redirect('flan_list') # Redirige a la lista de flanes
    else:
        form = FlanForm()
    return render(request, 'flan_form.html', {'form': form, 'is_edit': False})

@staff_member_required
def flan_update(request, pk):
    flan = get_object_or_404(Flan, pk=pk)
    if request.method == 'POST':
        form = FlanForm(request.POST, instance=flan)
        if form.is_valid():
            form.save()
            return redirect('flan_list')
    else:
        form = FlanForm(instance=flan)
    return render(request, 'flan_form.html', {'form': form, 'is_edit': True}) # Renderiza el template con el formulario y nos entrega una variable para reconocer si esta creando o actuañozando un flan

# Vista para eliminar un flan (requiere ser miembro del staff)
@staff_member_required
def flan_delete(request, pk):
    flan = get_object_or_404(Flan, pk=pk)  # Obtiene el flan por su clave primaria
    if request.method == 'POST':  # Si el formulario de confirmación ha sido enviado
        flan.delete()  # Elimina el flan de la base de datos
        return redirect('flan_list')  # Redirige a la lista de flanes
    return render(request, 'flan_confirm_delete.html', {'flan': flan})  # Renderiza el template de confirmación de eliminación