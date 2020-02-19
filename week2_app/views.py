from django.shortcuts import render
from django.http import HttpResponse

from .models import Course, Task

# Create your views here.
def index(request):
    courses = Course.objects.order_by('course_name')
    context = {"courses":courses}
    return render(request, 'index.html', context)