from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_home, name='login_home'),
    path('loggin', views.loggin, name='loggin'),
    path('registration', views.registration, name='registration')
]

