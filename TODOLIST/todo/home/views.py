from django.shortcuts import render, redirect
all_tasks = []
# Create your views here.


def homepage(request):
    for i in all_tasks:
        print(i)
    total_tasks = len(all_tasks)
    context = {
        'name': 'Hilda',
        'task_count': total_tasks,
        'all_tasks': all_tasks
    }
    return render(request, 'index.html', context)


def addTask(request):
    if request.method == 'POST':
        all_data = request.POST
        task = all_data['task_name']
        print(task)
        all_tasks.append(task)

    return redirect('/')
