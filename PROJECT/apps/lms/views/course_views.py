from django.shortcuts import render, get_object_or_404, redirect
from ..models import Course

# 📚 Course List
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'lms/course_list.html', {'courses': courses})


# 📖 Course Detail
def course_detail(request, id):
    course = get_object_or_404(Course, id=id)
    return render(request, 'lms/course_detail.html', {'course': course})


# ➕ Add Course
def add_course(request):
    if request.method == "POST":
        Course.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            instructor=request.POST['instructor']
        )
        return redirect('course_list')

    return render(request, 'lms/add_course.html')


# 👤 About Page
def about(request):
    return render(request, 'lms/about.html')