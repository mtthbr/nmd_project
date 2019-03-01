from django.contrib import admin
from django.urls import path, include



urlpatterns = [
  path('info_api/', include('info_api.urls')),
  path('festivaliers/', include('festivaliers.urls')),
  path('admin/', admin.site.urls),
]

