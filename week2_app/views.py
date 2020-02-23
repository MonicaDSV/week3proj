from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import ToDoForm, NewCourseForm
from .models import Course, Task

# Create your views here.
def index(request):
    addCourse = NewCourseForm()
    courses = Course.objects.order_by('course_name')
    taskForm = ToDoForm()
    context = {"courses":courses,'taskForm':ToDoForm, 'addCourse':NewCourseForm}

    return render(request = request, template_name= 'index.html',context= context)

#create about page here
def about(request):
    return render(request, 'about.html')

def post_course(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        ToDoForm_form = ToDoForm(request.POST)
        NewCourseForm_form = NewCourseForm(request.POST)
        # check whether it's valid:
        if ToDoForm.is_valid():
            # process the data in form.cleaned_data as required
            discription = ToDoForm.clean_data['description']
            time_due = ToDoForm.cleaned_data['time_due']
            # redirect to a new URL:
            return HttpResponseRedirect('')

        if NewCourseForm.is_valid():
            course_name = NewCourseForm.clean_data['course_name']

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewCourseForm()

    return render(request, 'base.html', {'form': form})

def post_task(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        ToDoForm_form = ToDoForm(request.POST)
        # check whether it's valid:
        if ToDoForm.is_valid():
            # process the data in form.cleaned_data as required
            discription = ToDoForm.clean_data['description']
            time_due = ToDoForm.cleaned_data['time_due']
            # redirect to a new URL:
            return HttpResponseRedirect('')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ToDoForm()

    return render(request, 'base.html', {'form': form})