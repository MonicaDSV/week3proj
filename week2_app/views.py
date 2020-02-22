from django.shortcuts import render
from django.http import HttpResponse

from .forms import ToDoForm
from .models import Course, Task

# Create your views here.
def index(request):
    courses = Course.objects.order_by('course_name')
    form = ToDoForm()
    context = {"courses":courses,'form':ToDoForm}
    return render(request, 'index.html', context)

#create about page here
def about(request):
    return render(request, 'about.html')

