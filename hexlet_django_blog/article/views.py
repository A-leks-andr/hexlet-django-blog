from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'app_name': 'hexlet_django_blog.article',
        'page_title': 'Главная страница блога',
        'welcome_message': 'Добро пожаловать в блог!',
    }
    return render(request, 'articles/index.html', context)