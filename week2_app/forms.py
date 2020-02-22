from django import forms
from .models import Task, Course


class ToDoForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description','time_due']

class NewCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields =['course_name']