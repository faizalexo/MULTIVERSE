from django.shortcuts import render, get_object_or_404
from ..models.course import Course


def home(request):
    query = request.GET.get('q')
    courses = Course.objects.all()

    if query:
        courses = courses.filter(title__icontains=query)

    return render(request, 'lms/dashboard.html', {
        'courses': courses,
        'query': query
    })


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'lms/course_list.html', {'courses': courses})


def course_detail(request, id):
    course = get_object_or_404(Course, id=id)
    return render(request, 'lms/pages/course_detail.html', {'course': course})