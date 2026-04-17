from django.shortcuts import render, get_object_or_404
from ..models.lesson import Lesson
from ..models.quiz import Quiz


def lesson_list(request):
    lessons = Lesson.objects.all().order_by('course', 'order')
    public_samples = Lesson.objects.filter(is_preview=True)[:3]
    quizzes = Quiz.objects.all()

    return render(request, 'lms/lesson_list.html', {
        'lessons': lessons,
        'public_samples': public_samples,
        'quizzes': quizzes
    })


def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)

    return render(request, 'lms/lesson_detail.html', {
        'lesson': lesson
    })