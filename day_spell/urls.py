from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_day_spell, name='day_spell'),
]