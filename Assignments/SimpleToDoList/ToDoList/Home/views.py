from django.shortcuts import render, redirect
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
        creationdate = form_data['creationdate']

        #to start a task objecf using the Tasklist model
        new_task = Tasklist()
        new_task.title = title
        new_task.description = description
        new_task.duedate = duedate
        new_task.priority = priority
        new_task.status = status
        new_task.creationdate = creationdate
        new_task.save()
        return redirect('/')

     return render(request, "add.html")

"""
def homePage(request):
    #for each task in all_tasks, their title will be printed to be seen by users 
    for task in all_tasks:
       print(task['title'])
    context = {
        'all_tasks': all_tasks
    }
    return render(request, "index.html", context)

#For the page for filling in the tasks

def addPage(request):
    if request.method == 'POST':
        form_data = request.POST
        title = form_data['title']
        description = form_data['description']
        duedate = form_data['duedate']
        priority = form_data['priority']
        status = form_data['status']
        
        #count all items in all_tasks and add 1, giving the tasks an id
        task_count = len(all_tasks)
        new_id = task_count + 1

        task = {
            'id':new_id,
            'title':title,
            'description':description,
            'duedate': duedate,
            'priority':priority,
            'status':status,
        } 

        #to see that the task doesn't exist
        isAlreadyCreated = False
        for each in all_tasks:
            if each['title'] == title:
                isAlreadyCreated = True
            else:
                continue
        if isAlreadyCreated == False:
            all_tasks.append(task)
            return redirect('/')
        else:
            context = {
                'error': "'The task '"+title+"' is already created"
            }
            return render(request, "add.html", context)
          
        all_tasks.append(task)
        return redirect('/')
    
    return render(request, "add.html")

"""