from django.shortcuts import render

def index(request):
    data = {
        'title': 'Главная страница',
    }
    return render(request, 'registr/index.html', data)

def about(request):
    return render(request, 'registr/about.html')

def login(request):
    return render(request, 'login/login_home.html')
