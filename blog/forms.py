from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() #default is required 

    class Meta: 
        model = User 
        fields = ['username', 'email', 'password']