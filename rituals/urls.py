from django.urls import path
from . import views


urlpatterns = [
    path('', views.ritual_list, name='ritual_list'),
    path('<int:pk>/', views.ritual_detail, name='ritual_detail'),
    path('add/', views.add_ritual, name='add_ritual'),
    path('edit/<int:ritual_id>/', views.update_ritual, name='update_ritual'),
]