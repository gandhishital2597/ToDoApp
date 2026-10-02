
from django.shortcuts import render
from todo.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed = False).order_by('-updated_at'  )
    #'-updated_at'  is means see the task in home page decending order

    completed_tasks = Task.objects.filter(is_completed = True)
    context = {
        'tasks':tasks,
        'completed_tasks' : completed_tasks
    }
    return render(request,'home.html',context)
