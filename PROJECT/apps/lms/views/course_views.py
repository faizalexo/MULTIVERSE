from django.shortcuts import render, get_object_or_404
from apps.lms.models import Course
from django.contrib.auth.decorators import login_required

@login_required
def course_list(request):
    return render(request, 'lms/course_list.html')

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'lms/course_list.html', {'courses': courses})

def course_detail(request, id):
    course = get_object_or_404(Course, id=id)
    return render(request, 'lms/course_detail.html', {'course': course})

# Add Course
def add_course(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        price = request.POST['price']
        Course.objects.create(title=title, description=description, price=price)
        return redirect('course_list')
    return render(request, 'lms/add_course.html')