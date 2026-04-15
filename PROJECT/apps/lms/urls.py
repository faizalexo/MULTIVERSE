from django.urls import path
from .views.dashboard_views import dashboard
from .views.course_views import course_list, course_detail

urlpatterns = [
    # 🏠 Dashboard
    path('', dashboard, name='dashboard'),  

    # 📚 Courses
    path('courses/', course_list, name='course_list'),
    path('courses/<int:id>/', course_detail, name='course_detail'),
    
]