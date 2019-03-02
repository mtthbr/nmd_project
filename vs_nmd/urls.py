from django.contrib import admin
from django.urls import path, include



urlpatterns = [
  path('info_api/', include('info_api.urls')),
  path('uservs/', include('uservs.urls')),
  path('admin/', admin.site.urls),
]

