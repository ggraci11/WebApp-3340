from django.urls import path, include
from . import views

urlpatterns = [
	path('',views.login_view, name = 'login'),
    path('home/', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('logout/', views.logout_view, name='logout'),
]