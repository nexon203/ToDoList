from django.shortcuts import render
from django.shortcuts import render, redirect
from tasks.forms import TaskForm
from tasks.models import Task
from django.shortcuts import render, get_object_or_404

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})


def task_list(request):
    tasks = Task.objects.filter(user=request.user.id)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/update_task.html', {'form': form, 'task': task})


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')


def pending_task(request):
    tasks = Task.objects.filter(status=False, user=request.user.id)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def completed_task(request):
    tasks = Task.objects.filter(status=True, user=request.user.id)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def done_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.status=True
    task.save()
    return redirect('task_list')