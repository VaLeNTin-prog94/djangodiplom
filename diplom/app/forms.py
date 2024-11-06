from django import forms
from .models import *


class AddPostFrom(forms.Form):
    title = forms.CharField(max_length=255)
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    is_published = forms.BooleanField()
    cat = forms.ModelChoiceField(queryset=Category.objects.all())


class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин')
    password = forms.CharField(min_length=8, label='Введите пароль')
    repeat_password = forms.CharField(min_length=8, label='Повторите пароль')
    age = forms.CharField(max_length=3, label='Введите свой возраст')

class UserLogin(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин')
    password = forms.CharField(min_length=8, label='Введите пароль')

