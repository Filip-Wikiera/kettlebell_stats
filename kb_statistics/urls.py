from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='kb_statistics'),
    path('kb_statistics/', views.index, name='kb_statistics'),
    path('calendar/', views.index, name='calendar'),
    path('add session/', views.session, name='add session'),
]
