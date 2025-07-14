from django.shortcuts import render, redirect

# Create your views here.

all_tasks = []

#For the first page
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


