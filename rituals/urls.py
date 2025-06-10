from django.urls import path
from . import views


urlpatterns = [
    path('', views.ritual_list, name='ritual_list'),
    path('<int:pk>/', views.ritual_detail, name='ritual_detail'),
]