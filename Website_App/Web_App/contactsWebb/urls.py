from django.urls import path, include
from . import views

urlpatterns = [
	path('',views.home, name = 'home'),
    path('login/', views.login_view, name='login'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),

]