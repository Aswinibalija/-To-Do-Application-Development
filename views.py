from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        Task.objects.create(
            tname=name,
            tdesc=desc
        ) 
        return redirect('home')
     

    tasks = Task.objects.all( )
    context = {
        'tasks' : tasks
    }
    return render(request,'home.html', context)


def update_task(request,pk):
    task=Task.objects.get(id=pk)
    if request.method == 'POST':
       
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        task.tname = name
        task.tdesc = desc
        task.save()
        return redirect('home')
    
    context = {
        'task':task
    }
    return render (request,'update.html',context)


def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete( )
    return redirect('home')

