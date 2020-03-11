from django.urls import path
from . import cbviews as views
from .views import csv_report

app_name = 'accounts'

urlpatterns = [
    path('', views.UserList.as_view(), name='list'),
    path('<str:username>', views.UserDetail.as_view(), name='detail'),
    path('add/', views.AddUser.as_view(), name='add'),
    path('edit/<str:username>', views.EditUser.as_view(), name='edit'),
    path('delete/<str:username>', views.DeleteUser.as_view(), name='delete'),
    path('report/', csv_report, name="report"),
]