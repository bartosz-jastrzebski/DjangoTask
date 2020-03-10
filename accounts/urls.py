from django.urls import path
from . import cbviews as views

app_name = 'accounts'

urlpatterns = [
    path('', views.UserList.as_view(), name='list'),
    path('add/', views.AddUser.as_view(), name='add'),
    path('edit/<str:username>', views.EditUser.as_view(), name='edit'),
    path('delete/', views.DeleteUser.as_view(), name='delete'),
    path('<str:username>/', views.UserDetail.as_view(), name='detail'),
    
]