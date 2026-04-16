from django.contrib import admin
from django.urls import path, include
from apps.worldmonitor import views



urlpatterns = [
    path('', views.index, name='home'),
    path('cyberattacks/', views.cyberattacks),
    path('geopolitics/', views.geopolitics),
    path('country/<str:country>/', views.country_news),
]

