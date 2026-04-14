from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/', include('apps.accounts.urls')),
    path('shop/', include('apps.ecommerce.urls')),
    path('learn/', include('apps.lms.urls')),
    path('world/', include('apps.worldmonitor.urls')),
]