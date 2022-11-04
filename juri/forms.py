# -*- coding: utf-8 -*-
from django import forms
# from .models import Contact


class search_Form(forms.Form):
	search = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)