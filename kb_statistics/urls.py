from django.urls import path
from . import views
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='kb_statistics'),
    path('kb_statistics/', views.index, name='kb_statistics'),
    path('calendar/', views.index, name='calendar'),
    path('add session/', views.index, name='add session'),

]
