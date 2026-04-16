from django.contrib import admin
from django.urls import path
from apps.worldmonitor.views import index, cyberattacks, geopolitics, country_news

urlpatterns = [
    path('', index, name='home'),
    path('world/', index),
    

    path('cyberattacks/', cyberattacks),
    path('geopolitics/', geopolitics),

    path('country/<str:country>/', country_news),
]


