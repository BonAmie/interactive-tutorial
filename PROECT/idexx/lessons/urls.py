from django.urls import path
from . import views

urlpatterns = [
    path('', views.lessons_home, name='lessons_home'),
    path('<int:pk>', views.LessDetailView.as_view(), name='less-detail')
]

