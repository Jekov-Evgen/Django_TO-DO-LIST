from django.urls import path
from . import views
from TASK.views import creation_task, delete_task

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('homepage/', views.homepage, name='homepage'),
    path('add_task/', creation_task, name='add_task'),
    path('dell_task/', delete_task, name='del_task')
]