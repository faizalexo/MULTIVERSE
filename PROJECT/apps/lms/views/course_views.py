from django.shortcuts import render, get_object_or_404
from ..models import Course


def home(request):
    courses = Course.objects.all()
    return render(request, 'lms/dashboard.html', {'courses': courses})


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'lms/course_list.html', {'courses': courses})


def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)

    lessons = course.lessons.all()
    quizzes = course.quizzes.all()

    return render(request, 'lms/course_detail.html', {
        'course': course,
        'lessons': lessons,
        'quizzes': quizzes
    })