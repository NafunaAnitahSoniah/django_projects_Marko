from django.shortcuts import render, get_object_or_404, redirect
from Home.models import Tasklist

# Create your views here.

def homePage(request):
    all_tasks = Tasklist.objects.all()
    for task in all_tasks:
        print(task.title)
        
    context = {
        "all_tasks": all_tasks
    }
    return render(request, "index.html", context)


def addPage(request):
     if request.method == 'POST':
        form_data = request.POST
       
        #to fetch form data
        title = form_data['title']
        description = form_data['description']
        duedate = form_data['duedate']
        priority = form_data['priority']
        status = form_data['status']
        

        #to start a task objecf using the Tasklist model
        new_task = Tasklist()
        new_task.title = title
        new_task.description = description
        new_task.duedate = duedate
        new_task.priority = priority
        new_task.status = status      
        new_task.save()
        return redirect('/')

     return render(request, "add.html")


def updateTask(request, task_id):
    task = get_object_or_404(Tasklist, id=task_id)

    if request.method == 'POST':
        task.priority = request.POST.get('priority')
        task.status = request.POST.get('status')
        task.save()
        return redirect('/')

    return render(request, 'updateTask.html', {'task': task})


def deleteTask(request, task_id):
    task = get_object_or_404(Tasklist, id=task_id)

    if request.method == 'POST':
        task.delete()
        return redirect('/')  # Redirect after delete

    # GET request shows confirmation page
    return render(request, 'deleteTask.html', {'task': task})
