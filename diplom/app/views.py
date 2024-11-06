from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить статью", 'url_name': 'add_page'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    {'title': "Регистрация", 'url_name': 'registration'},
    {'title': "Войти", 'url_name': 'login'},

]


def index(request):
    post = Bake.objects.all()
    cats = Category.objects.all()
    data = {
        'cats': cats,
        'post': post,
        "menu": menu,
        "title": 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'index.html', context=data)


def about(request):
    return render(request, 'about.html', {'menu': menu, 'title': 'О сайте'})


def addpage(request):
    if request.method == 'POST':
        form = AddPostFrom(request.POST)
        if form.is_valid():
            try:
                Bake.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка добавления поста')

    else:
        form = AddPostFrom()
    return render(request, 'add_page.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})


def contact(request):
    return render(request, 'contact.html', { 'menu': menu, 'title': 'Обратная связь'})


def registration(request):
    users = User.objects.all()
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password == repeat_password and int(age) >= 18 and username not in [b.username for b in users]:
                User.objects.create(username=username, password=password, age=age)
                return render(request, 'registrationsuccesfull.html', {'menu': menu, 'user': username})
            elif password != repeat_password:
                return HttpResponse(f'<h1>Пароли не совпадают</h1>')
            elif int(age) < 18:
                return HttpResponse(f'<h1>Вы должны быть старше 18</h1>')
            elif username in [b.username for b in users]:
                return HttpResponse( f'<h1>Пользователь {username} уже существует</h1>')
    else:
        form = UserRegister()
    return render(request, 'registration.html', { 'menu': menu, 'title': 'Регистрация пользователей'})


def login(request):
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if name not in [b.username for b in User.objects.all()]:
                return HttpResponse(f'<h1>Такого пользователя не существует</h1>')
            else:
                users = User.objects.get(username=name)
                if users.password != password:
                    return HttpResponse(f'<h1>Ввели не правильный пароль, повторите попытку</h1>')
                else:
                    return render(request, 'usersuccesfull.html', {'menu': menu, 'user': name})
    else:
        form = UserLogin()
    return render(request, 'login.html', context={'menu': menu, 'title': 'Регистрация пользователя'})


def show_post(request, post_id):
    post = get_object_or_404(Bake, pk=post_id)

    data = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id
    }
    return render(request, 'post.html', context=data)


def show_category(request, cat_id):
    post = Bake.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    data = {
        'post': post,
        'cats': cats,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }
    return render(request, 'index.html', context=data)
