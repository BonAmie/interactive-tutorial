from .models import Tasks
from django.forms import ModelForm

class ArticlesForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'intro', 'full_text']

