from django.shortcuts import render, get_object_or_404
from apps.lms.models import Course

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'lms/course_list.html', {'courses': courses})

def course_detail(request, id):
    course = get_object_or_404(Course, id=id)
    return render(request, 'lms/course_detail.html', {'course': course})