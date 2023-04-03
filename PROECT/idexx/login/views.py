from django.shortcuts import render
from .models import Login

def login_home(request):
    log = Login.objects.all()
    data = {
        'title': 'Личный кабинет',
    }
    return render(request, 'registr/index.html', data)

def loggin(request):
    return render(request, 'login/loggin.html')

def registration(request):
    return render(request, 'login/registration.html')
