from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    """Form for creating new tasks"""
    class Meta:
        model = Task
        fields = ['title','notes']
        labels = {'title':'Title','notes':'Notes'}
        
