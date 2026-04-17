from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from ..models.course import Course
from ..models.quiz import Quiz, Question, Choice


def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    question = quiz.questions.order_by('order').first()

    return render(request, 'lms/quiz_detail.html', {
        'quiz': quiz,
        'question': question,
    })


def course_quiz_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    quizzes = course.quizzes.all()

    return render(request, 'lms/course_detail.html', {
        'course': course,
        'quizzes': quizzes
    })


def submit_answer(request):
    if request.method == "POST":
        import json
        data = json.loads(request.body)

        choice = get_object_or_404(Choice, id=data.get('choice_id'))
        question = get_object_or_404(Question, id=data.get('question_id'))

        is_correct = choice.is_correct

        next_q = Question.objects.filter(
            quiz=question.quiz,
            order__gt=question.order
        ).order_by('order').first()

        return JsonResponse({
            'correct': is_correct,
            'next_question_id': next_q.id if next_q else None,
            'feedback': (
                "Correct!" if is_correct
                else f"Incorrect. Correct answer: {question.choices.filter(is_correct=True).first().text}"
            )
        })


def quiz_home(request):
    courses = Course.objects.prefetch_related('quizzes')
    return render(request, 'lms/quiz_home.html', {
        'courses': courses
    })