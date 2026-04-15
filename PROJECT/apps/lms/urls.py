from django.urls import path
from .views.dashboard_views import dashboard
from .views.course_views import course_list, course_detail, add_course, about
from .views.quiz_views import quiz_view

urlpatterns = [
    # 🏠 Dashboard
    path('', dashboard, name='dashboard'),

    # 📚 Courses
    path('courses/', course_list, name='course_list'),
    path('courses/<int:id>/', course_detail, name='course_detail'),

    # ➕ Add Course
    path('add-course/', add_course, name='add_course'),

    # 👤 About
    path('about/', about, name='about'),

    # 🧪 Quiz
    path('quiz/<int:course_id>/', quiz_view, name='quiz'),
]