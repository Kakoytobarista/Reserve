from django.shortcuts import render


def login_index(request):
    return render(request, 'accounts/base.html')
