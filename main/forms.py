from django import forms
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class JoinForm(forms.ModelForm):
    # login = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255, help_text='Это обязательное поле')
    password = forms.CharField(max_length=255)
    login = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'login')
