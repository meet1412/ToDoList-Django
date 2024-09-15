from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from home.models import Task

# View to handle the home page, where tasks can be created
def home(request):
    # Check if the request method is POST, which means the form was submitted
    if request.method == "POST":
        # Retrieve task title and description from the form data
        task = request.POST['task']
        desc = request.POST['desc']
        
        # Create a new Task object and save it to the database
        ins = Task(taskTitle=task, taskDesc=desc)
        ins.save()
        
        # Pass a success flag to the template
        context = {'success': True}
    else:
        # If not a POST request, set the success flag to False
        context = {'success': False}
        
    # Render the home page template with the context data
    return render(request, 'index.html', context)



# View to display a list of all tasks
def task(request):
    # Retrieve all Task objects from the database
    allTask = Task.objects.all()
    
    # Pass the tasks to the template context
    context = {'task': allTask}
    
    # Render the task list template with the context data
    return render(request, 'task.html', context)



# View to handle updating a specific task
def update(request, id):
    # Retrieve the Task object with the given id, or return a 404 error if not found
    allTask = get_object_or_404(Task, id=id)
    
    # Pass the task to the template context
    context = {'task': allTask}
    
    # Check if the request method is POST, which means the form was submitted
    if request.method == 'POST':
        # Update the task's title and description with the form data
        allTask.taskTitle = request.POST.get('task')
        allTask.taskDesc = request.POST.get('desc')
        
        # Save the updated task to the database
        allTask.save()
        
        # Redirect to the task list page after updating
        return redirect('task')
    
    # Render the update form template with the context data
    return render(request, 'update.html', context)



# View to handle deleting a specific task
def delete(request, id):
    # Retrieve the Task object with the given id, or return a 404 error if not found
    allTask = get_object_or_404(Task, id=id)
    
    # Pass the task to the template context
    context = {'task': allTask}
    
    # Check if the request method is POST, which means the form was submitted
    if request.method == 'POST':
        # Delete the task from the database
        allTask.delete()
        
        # Redirect to the task list page after deletion
        return redirect('task')
    
    # Render the delete confirmation template with the context data
    return render(request, 'delete.html', context)