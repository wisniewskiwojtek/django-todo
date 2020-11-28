from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('task_list/',views.task_list,name='task_list'),
    path('create_task/',views.create_task,name='create_task'),
    path('edit_task/<task_id>/',views.edit_task,name='edit_task'),
    # path('delete_task/<task_id>',views.delete_task,name='delete_task')
]
app_name = 'todos'