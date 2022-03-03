
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Post

class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()
    password1=forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirmar Contraseña',widget=forms.PasswordInput)

    class Meta:
        model = User
        #
        fields= ['username','email','password1','password2']
        #eliminar todos las decripcion de ayuda para ingresar contraseña
        help_texts={k:"" for k in fields}


class PostForm(forms.ModelForm):
    contenido=forms.CharField(label='',widget=forms.Textarea(attrs={'rows':2,'placeholder':'¿Que esta pasando?'}),required=True)

    class Meta:
        model=Post
        fields=['contenido']