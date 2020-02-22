from django import forms
from .models import Task, Course


class ToDoForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description','time_due']





