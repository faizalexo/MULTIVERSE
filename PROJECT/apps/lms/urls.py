from django.urls import path
from apps.lms.views.course_views import home, course_list, course_detail
from apps.lms.views.lesson_views import lesson_list, lesson_detail
from apps.lms.views.quiz_views import quiz_home, quiz_detail, submit_answer

app_name = 'lms'

urlpatterns = [

    # 🔥 THIS FIXES /learn/
    path('', home, name='home'),

    path('courses/', course_list, name='course_list'),
    path('courses/<slug:slug>/', course_detail, name='course_detail'),

    path('lessons/', lesson_list, name='lesson_list'),
    path('lesson/<int:lesson_id>/', lesson_detail, name='lesson_detail'),

    path('quiz/', quiz_home, name='quiz_home'),
    path('quiz/<int:quiz_id>/', quiz_detail, name='quiz_detail'),

    path('submit-answer/', submit_answer, name='submit_answer'),
  


]