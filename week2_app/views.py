from django.shortcuts import render
from django.http import HttpResponse

from .forms import ToDoForm, NewCourseForm
from .models import Course, Task

# Create your views here.
def index(request):
    addCourse = NewCourseForm()
    courses = Course.objects.order_by('course_name')
    taskForm = ToDoForm()
    context = {"courses":courses,'taskForm':ToDoForm, 'addCourse':NewCourseForm}
    return render(request, 'index.html', context)

#create about page here
def about(request):
    return render(request, 'about.html')

