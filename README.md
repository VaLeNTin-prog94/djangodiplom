## Проект Django Diplom
Веб приложение предназначенное для управления постами о выпечках. 

## Содержание
Оно предлагает интуитивно понятный интерфейс для создания, редактирования, удаления и обновления записей используя архитектуру MVT(Model-View-Templates)
Модели обрабатывают данные, представления управляют логикой, а шаблоны отражают информацию пользователя
Django Form для обработки форм и добавления записей в базу данных
Пользовательские функции регистрации и входа в систему

## Использование
Установите django  с помощью команды:
```
pip install django 
```

## Разработка
Создаем проект 
```
django-admin startproject diplom
```
Переходим в директиву проекта
```
cd diplom:
```
Запуск сервера осуществляется по команде:
```
 python manage.py startapp app
```
Для обработка изображений нужно скачать библиотеку Pillow
```
python -m pip install Pillow 
```
Создаем admina для управления веб приложением :
```
python manage.py createsuperuser  
```

##Для миграции таблиц базы данных пишем команы:
```
python manage.py migrate  
```
```
python manage.py makemigrations  
```

## URL использованные в проекте
```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('add_page/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category'),
]
```
##Зачем вы разработали этот проект?
Для защиты дипломной работы

## Команда проекта
Валентин Михайлов

## Источники
Вдохновлялся книгами Дронова о Джанго
- https://django.fun/docs/django/5.0/topics/forms/
