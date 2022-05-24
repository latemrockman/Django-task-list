from django.shortcuts import render
from . models import Task
# Create your views here.


def index(request):
    all_tasks = Task.objects.order_by('-id')
    title_page = 'Главная страница'
    return render(request, 'main/index.html', {'all_tasks': all_tasks, 'title_page': title_page})

def create_task(request):
    title_page = 'Добавить задачу'
    return render(request, 'main/create_task.html', {'title_page': title_page})



def about(request):
    title_page = 'Информация о нас'
    return render(request, 'main/about.html', {'title_page': title_page})