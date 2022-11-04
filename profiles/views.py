from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# from .models import Contact
from .forms import ContactForm, LoginForm


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("juri:index"))

def login_view(request):
    """ Login """
    form = LoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username_form = form.cleaned_data['username']
            password = form.cleaned_data['password']
            usuario = authenticate(username=username_form,password=password)
            if usuario is not None:
                login(request,usuario)
                # the password verified for the user
                return HttpResponseRedirect(reverse("juri:index"))
            else:
                messages.warning(request, 'Usuario y/o password errado')
    ctx = {'form': form}
    return render(request, 'login.html', ctx)

def contactanos_view(request):
    """ Contactanos """
    form = ContactForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, f'Tu mensaje ha sido enviado.')
            return HttpResponseRedirect(reverse("profiles:contactanos"))
    ctx = {'form': form}
    return render(request, 'contactanos.html', ctx)
