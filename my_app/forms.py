from django import forms
from .models import RegisterForm

class MyRegisterForm(forms.ModelForm):
    class Meta:
        model = RegisterForm
        fields = ["name","age","designation","salary","email","mobile"]




