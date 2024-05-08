from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .forms import *
from .models import *
from .utils import *


class ArticleIndex(DataMixin, ListView):
    paginate_by = 3
    model = Article
    template_name = 'general/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Article.objects.filter(is_published=True)


class ArticleCategory(DataMixin, ListView):
    model = Article
    template_name = 'general/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        d_cef = self.get_user_context(title=context['posts'][0].category,
                                      cat_selected=context['posts'][0].category_id)
        return dict(list(context.items()) + list(d_cef.items()))

    def get_queryset(self):
        return Article.objects.filter(category__slug=self.kwargs['category_slug'], is_published=True)


class ArticlePost(DataMixin, DetailView):
    model = Article
    template_name = 'general/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Статья - ' + str(context['post']), cat_selected=None)
        return dict(list(context.items()) + list(c_def.items()))


class ArticleAddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'general/addpage.html'
    success_url = reverse_lazy('general')
    login_url = reverse_lazy('general')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление статьи')
        return dict(list(context.items()) + list(c_def.items()))


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def about(request):
    contact_list = Article.objects.all()
    paginator = Paginator(contact_list, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
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
