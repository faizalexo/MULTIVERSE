from django.shortcuts import render, get_object_or_404
from ..models import Course


def home(request):
    courses = Course.objects.all()
    return render(request, 'lms/dashboard.html', {'courses': courses})


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'lms/course_list.html', {'courses': courses})


def course_detail(request, slug):
    course = Course.objects.get(slug=slug)
    lessons = course.lessons.all()

    return render(request, 'lms/course_detail.html', {
        'course': course,
        'lessons': lessons,
        'first_video': lessons.first()
    })