from django.urls import path
from .views import course_views

urlpatterns = [
    path('', course_views.course_list, name='lms_home'),
]