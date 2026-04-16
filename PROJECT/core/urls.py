from django.contrib import admin
from django.urls import path, include
from apps.lms.views.dashboard_views import dashboard
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # 🔥 MASTER (default home)
    path('', include('apps.master.urls')),

    # 🔐 AUTH SYSTEM
    path('', include('apps.accounts.urls')),

    # 🛒 APPS
    path('shop/', include('apps.ecommerce.urls')),
    path('learn/', include('apps.lms.urls')),
    path('world/', include('apps.worldmonitor.urls')),
]




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

