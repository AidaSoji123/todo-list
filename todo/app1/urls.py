from django.urls import path
from . import views

app_name = "app1"
urlpatterns = [   
   path('signup',views.signup, name='signup'),
   path('login',views.login, name='login'),
   path('index',views.index, name='index'),
   path('task',views.task, name='task'),
   path('reset',views.reset, name='reset'),
   path('delete_task/<int:task_id>',views.delete_task, name='delete_task'),
   path('update_status/<int:task_id>',views.update_status,name="update_status"),
   path('edit_task/<int:task_id>',views.edit_task,name="edit_task"),
]