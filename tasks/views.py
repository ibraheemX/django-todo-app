from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import Taskform


def tasks(request):
    all_tasks = Task.objects.all()
    tasks_count = all_tasks.count()

    if request.method == 'POST':
        form = Taskform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    else:
        form = Taskform()

    context = {
        'tasks': all_tasks,
        'count': tasks_count,
        'form': form,
    }
    return render(request, 'tasks/task_list.html', context)


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('tasks')


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        form = Taskform(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    else:
        form = Taskform(instance=task)

    return render(request, 'tasks/edit_task.html', {'form': form, 'task': task})
