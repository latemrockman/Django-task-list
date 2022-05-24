from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_task, name='create-task'),
    path('about/', views.about, name='about')
]


