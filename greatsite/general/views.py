from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *
menu = ['О сайте', 'Добавить статью', 'Обратная свяь', 'Войти']


def index(request):
    posts = Music.objects.all()
    return render(request, 'general/index.html',
                  {'title': 'Главная страница',
                   'menu': menu,
                   'posts': posts})


def about(request):
    return render(request, 'general/about.html',
                  {'about': 'О сайте.', 'menu': menu})


def categories(request, categories_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse('<h1>Страница категорий.</h1>'
                        f'<p>{categories_slug}</p>')


def archive(request, year):
    if int(year) > 2024:
        return redirect("general", permanent=True)
    return HttpResponse("<h1>Страница архива.</h1>"
                        f"Год - {year}.")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Данной страницы не существует.</h1>'
                                'Ошибка 404.')
