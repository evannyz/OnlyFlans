from django import forms
from .models import ContactForm, Flan
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Formulario de contacto sin modelo
class ContactFormForm(forms.Form):
    customer_email = forms.EmailField(label='Correo')
    customer_name = forms.CharField(max_length=64, label='Nombre')
    message = forms.CharField(label='Mensaje')

# Formulario de contacto basado en un modelo
class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email', 'customer_name','message']
        widgets = {
            'customer_email': forms.EmailInput()
        }

# Formulario de creación de usuario personalizado
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

# Formulario para el modelo Flan
class FlanForm(forms.ModelForm):
    class Meta:
        model = Flan
        fields = ['name', 'description', 'image_url', 'slug', 'is_private','price']