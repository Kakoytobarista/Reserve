from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect


class LoginPage(LoginView):
    redirect_authenticated_user = '/main/'
    template_name = 'accounts/login_form.html'
