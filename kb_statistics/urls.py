from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='kb_statistics'),
    path('kb_statistics/', views.index, name='kb_statistics'),
    path('calendar/', views.CalendarView, name='calendar'),
    path('event/edit/<int:pk>/', views.edit_session, name='event_edit'),
    # path('event/delete/<int:pk>/', EventDeleteView.as_view(), name='event_delete'),
    path('add session/', views.session, name='add session'),
]
