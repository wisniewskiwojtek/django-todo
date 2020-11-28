from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('task/list/',views.task_list,name='task_list'),
    path('task/create/',views.create_task,name='create_task'),
    path('task/edit/<task_id>/',views.edit_task,name='edit_task'),
    path('task/delete/<task_id>',views.delete_task,name='delete_task')
]
app_name = 'todos'