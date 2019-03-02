from django.urls import path
from . import views


urlpatterns = [
  path('artistes/', views.ArtisteListCreate.as_view() ),
  path('Solexs/', views.SolexListCreate.as_view() ),
  path('notifications/', views.NotificationListCreate.as_view() ),
  path('descriptions/', views.DescriptionListCreate.as_view() ),
]