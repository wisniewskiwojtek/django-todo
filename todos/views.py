from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from .models import Task
from .forms import TaskForm
# Create your views here.
def index(request):
    return render(request,'todos/index.html')

def task_list(request):
    t_list = Task.objects.all().order_by('-date_added')
    context = {'task_list':t_list}
    return(render(request,'todos/task_list.html',context))

def create_task(request):
    """Creates new task"""
    
    if(request.method != 'POST'):
        form = TaskForm()
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid():
            form.save()
            return(HttpResponseRedirect(reverse('todos:task_list')))
    
    context = {'form':form}
    return render(request,'todos/create_task.html',context)

def edit_task(request,task_id):
    """Edits task"""
    task = Task.objects.get(id=task_id)

    #if it is get request
    if request.method != 'POST':
        form = TaskForm(instance= task)
    else:
        form = TaskForm(data=request.POST,instance=task)
        if(form.is_valid):
            form.save()
            return(HttpResponseRedirect(reverse('todos:task_list')))
    context={'form':form,'task_id':task_id}
    return render(request,'todos/edit_task.html',context)

def delete_task(request,task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return HttpResponseRedirect(reverse('todos:task_list'))
    