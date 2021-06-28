from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterUserForm


class LoginPage(LoginView):
    redirect_authenticated_user = '/main/'
    template_name = 'accounts/login_form.html'


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'accounts/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')

