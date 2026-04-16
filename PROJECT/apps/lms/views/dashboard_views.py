from django.shortcuts import render
from ..models import Course

def dashboard(request):
    courses = Course.objects.all()
    return render(request, 'lms/dashboard.html', {'courses': courses})

def home(request):
    return render(request, 'home.html')