from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView


class LoginPage(LoginView):
    redirect_authenticated_user = '/main/'
    template_name = 'accounts/login_form.html'


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')
