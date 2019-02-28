from django.contrib import admin
from django.urls import path

from festivaliers.views import fetch_festivaliers

urlpatterns = [
  path('admin/', admin.site.urls),
  path('fetch_festivaliers/', fetch_festivaliers)
]