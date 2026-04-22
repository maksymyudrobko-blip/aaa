
from . import views
from django.urls import path
urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.board_list_view, name='board_list'),
    path('board/create/', views.board_create_view, name='board_create'),
    path('board/<int:board_id>/', views.board_detail_view, name='board_detail'),
    path('board/<int:board_id>/task/add/', views.task_create_view, name='task_create'),
    path('task/<int:task_id>/', views.task_detail_view, name='task_detail'),
    path('task/<int:task_id>/edit/', views.task_edit_view, name='task_edit'),
]