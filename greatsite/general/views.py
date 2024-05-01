from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_article'},
        {'title': 'Обратная связь', 'url_name': 'feedback'},
        {'title': 'Войти', 'url_name': 'login'}]
blender_posts = [Music.objects.all(),
                 Movie.objects.all(),
                 VideoGame.objects.all()]


def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}')


def show_category(request, category_id):
    flag = False
    for i in blender_posts:
        if i.filter(category_id=category_id):
            posts = i
            flag = True
    cats = Category.objects.all()
    if not flag:
        raise Http404()
    dir_context = {
        'posts': posts,
        'menu': menu,
        'title': 'Cтатьи по рубрике.',
        'cats': cats,
        'cat_selected': category_id
    }
    return render(request, 'general/index.html', context=dir_context)


def add_article(request):
    return HttpResponse('Добавляем статью')


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def index(request):
    posts = []
    for i in blender_posts:
        for j in i[:3]:
            posts.append(j)
    cats = Category.objects.all()
    dir_context = {
        'posts': posts,
        'menu': menu,
        'title': menu[0]['title'],
        'cats': cats,
        'cat_selected': 0
    }
    return render(request, 'general/index.html', context=dir_context)


def about(request):
    dir_context = {
        'menu': menu,
        'title': 'О сайте'
    }
    return render(request, 'general/about.html', context=dir_context)


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
