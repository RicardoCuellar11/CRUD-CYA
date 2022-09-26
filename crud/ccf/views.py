from django.shortcuts import render
from ccf.models import ccf
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'ccf/index.html')


class ccfListado(ListView):
    model = ccf


class ccfCrear(SuccessMessageMixin, CreateView):
    model = ccf
    form = ccf
    fields = "__all__"
    success_message = "Usuario creado correctamente"

    def get_success_url(self):
        return reverse('')


class ccfDetalle(DetailView):
    model = ccf


class ccfActualizar(SuccessMessageMixin, UpdateView):
    model = ccf
    form = ccf
    fields = "__all__"
    success_message = 'Usuario actualizado correctamente'

    def get_success_url(self) -> str:
        return reverse('')


class ccfEliminar(SuccessMessageMixin, DeleteView):
    model = ccf
    form = ccf
    fields = "__all__"

    def get_success_url(self):
        success_message = 'Usuario eliminado correctamente'
        messages.success(self.request, (success_message))
        return reverse('')
