from django import forms
from .models import Guest
from django.forms import TextInput, Select

class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest

        fields = [
            "first_name",
            "last_name",
            "email",
            "gender",
            "id_number"
        ]

        widgets = {
             'first_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 60%;',
                'placeholder': 'First Name'
                }),
                'last_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 60%;',
                'placeholder': 'Your lastname'
                }),
                'email': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 60%;',
                'placeholder': 'Your email'
                }),
                'gender': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 60%;',
                'placeholder': 'Gender'
                }),
                'id_number': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 60%;',
                'placeholder': '1245678'
                }),
        }