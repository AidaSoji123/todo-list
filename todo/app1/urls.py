from django.urls import path
from . import views

app_name = "app1"
urlpatterns = [   
   path('signup',views.signup, name='signup'),
   path('login',views.login, name='login'),
   path('index',views.index, name='index'),
   path('task',views.task, name='task'),
   path('reset',views.reset, name='reset'),
]