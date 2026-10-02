from django.shortcuts import redirect

from .models import *

# Create your views here.

def addTask(request):
    task = request.POST['task']
    Task.objects.create( #create crud operation to create task in django admin
        task=task

    )
    return redirect('home')