from django.shortcuts import redirect, render, HttpResponse
from home.models import Task

# Create your views here.
def home(request):
            
    if request.method == "POST":
        task = request.POST['task']
        desc = request.POST['desc']
        ins = Task(taskTitle=task, taskDesc=desc)
        ins.save()
        context = {'success': True}
    else:
        context = {'success': False}
        
    return render(request, 'index.html', context)

def task(request):
    allTask = Task.objects.all()
    context = {'task': allTask}
    return render(request, 'task.html', context)
