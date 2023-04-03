from django.shortcuts import render
from .models import Tasks
from .forms import ArticlesForm
from django.views.generic import DetailView

class LessDetailView(DetailView):
    model = Tasks
    template_name = 'lessons/details_view.html'
    context_object_name = 'article'


def lessons_home(request):
    less = Tasks.objects.order_by('title')
    return render(request, 'lessons/lessons_home.html', {'less': less})

