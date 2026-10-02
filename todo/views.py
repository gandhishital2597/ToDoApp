from django.http import HttpResponse

from django.shortcuts import redirect,render, get_object_or_404

from .models import *

# Create your views here.

#create
def addTask(request):
    task = request.POST['task']
    Task.objects.create( #create crud operation to create task in django admin
        task=task

    )
    return redirect('home')

#create crud operation to read task
def mark_as_done(request,pk):
    task = get_object_or_404(Task,pk=pk) #get data from database
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request,pk):
    task = get_object_or_404(Task, pk=pk)  # get data from database
    task.is_completed = False
    task.save()
    return redirect('home')

#edit operation/update
def edit_task(request,pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_task' : get_task
        }
        return render(request,'edit_task.html',context)

#delete feature
def delete_task(request,pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete() #delete in built feature
    return redirect('home')



