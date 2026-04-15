from django.shortcuts import render
from ..models import Quiz

def quiz_view(request, course_id):
    quizzes = Quiz.objects.filter(course_id=course_id)
    return render(request, 'lms/quiz.html', {'quizzes': quizzes})