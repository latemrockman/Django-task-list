from django.shortcuts import render
from . models import Task
# Create your views here.


def index(request):
    all_tasks = Task.objects.all()
    title_page = 'Главная страница'
    return render(request, 'main/index.html', {'all_tasks': all_tasks, 'title_page': title_page})


def about(request):
    title_page = 'Информация о нас'
    return render(request, 'main/about.html', {'title_page': title_page})