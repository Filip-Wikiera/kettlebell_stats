from django.urls import path
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='kb_statistics'),
    path('kb_statistics/', views.index, name='kb_statistics'),
    path('calendar/', views.index, name='calendar'),
    path('add session/', views.index, name='add session'),
    path('profile/', views.index, name='profile'),
    path('logout/', views.index, name='logout'),
    path('login/', views.index, name='login'),
    path('register/', views.index, name='register'),
]
