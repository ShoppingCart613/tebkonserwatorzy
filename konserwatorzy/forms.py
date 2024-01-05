from django import forms
from .models import Zadanie

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ZadanieForm(forms.ModelForm):
    class Meta:
        model = Zadanie
        fields = ('nazwa', 'opis', 'stan')
