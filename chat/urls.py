from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Chat Administration"
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.accounts.api.urls')),
    path('api/threads/', include('apps.core.api.urls')),
]
