# -*- coding: utf-8 -*-
from django import forms
from .models import Contact


class LoginForm(forms.Form):
  username = forms.CharField(max_length=75, required=True, widget=forms.TextInput(), label='Usuario')
  password = forms.CharField(required=True, widget=forms.PasswordInput(render_value=False))

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['nombres', 'email', 'titulo', 'contenido']
        widgets = {
          'contenido': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
        }