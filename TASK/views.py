from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from .models import TaskList

@login_required
def creation_task(request):
    if request.method == 'POST':
        task_name = request.POST.get('task_name')
        if task_name:
            try:
                max_number_task = TaskList.objects.filter(user=request.user).aggregate(Max('number_task'))['number_task__max']
                if max_number_task is None:
                    max_number_task = 0
                new_task_number = max_number_task + 1
                new_task = TaskList.objects.create(name_task=task_name, user=request.user, number_task=new_task_number)
                print(f"Новая задача добавлена: {new_task.name_task} с номером {new_task.number_task}")
            except Exception as e:
                print(f"Ошибка при сохранении задачи: {e}")
            return redirect('homepage')
    tasks = TaskList.objects.filter(user=request.user)
    return render(request, 'accounts/homepage.html', {'username': request.user.username, 'tasks': tasks})

@login_required
def delete_task(request):
    if request.method == 'POST':
        task_number = request.POST.get('task_number')
        print(f"Получен номер задачи для удаления: {task_number}")  # Отладочное сообщение
        if task_number:
            try:
                task_to_delete = get_object_or_404(TaskList, user=request.user, number_task=task_number)
                task_to_delete.delete()
                print(f"Задача с номером {task_number} успешно удалена")
            except Exception as e:
                print(f"Ошибка при удалении задачи: {e}")
    else:
        print("Метод запроса не POST") 
    return redirect('homepage')
