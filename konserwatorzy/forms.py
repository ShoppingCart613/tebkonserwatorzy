from django import forms
from .models import Zadanie

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    widgets = {
        username: forms.TextInput(attrs={'class':'form-control'}),
        password: forms.TextInput(attrs={'class':'form-control'}),
    }

class ZadanieForm(forms.ModelForm):
    class Meta:
        model = Zadanie
        fields = ('nazwa', 'opis', 'stan', 'waznosc')

        widgets = {
            'nazwa': forms.TextInput(attrs={'class':'form-control'}),
            'opis': forms.Textarea(attrs={'class':'form-control'}),
            'stan': forms.Select(attrs={'class':'form-control'}),
            'waznosc': forms.Select(attrs={'class':'form-control'}),
        }

class ZadanieEditForm(forms.ModelForm):
    class Meta:
        model = Zadanie
        fields = ('nazwa', 'opis', 'stan', 'waznosc')

        widgets = {
            'nazwa': forms.TextInput(attrs={'class':'form-control'}),
            'opis': forms.Textarea(attrs={'class':'form-control'}),
            'stan': forms.Select(attrs={'class':'form-control'}),
            'waznosc': forms.Select(attrs={'class':'form-control'}),
        }
