from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from . models import Task

# Create your views here.


def addTask(request):
    task = request.POST['task'] # here task is the name variable.
    Task.objects.create(task=task, updated_at = task) # task is the field name v=which can store the value stored in the task variable by post request.
    return redirect('home')


def mark_as_done(request,pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

    
def mark_as_undone(request,pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

# when the click on the edit icon then get request is coming on the page and edit page is open.
# when we edited the task then post request will be done.
def edit_task(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_task': get_task,
        }
        return render(request, "edit.html", context)
    



def delete_task(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    get_task.delete()
    return redirect('home')
