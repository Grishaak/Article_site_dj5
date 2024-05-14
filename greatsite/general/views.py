from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from .forms import *
from .models import *
from .utils import *


class ArticleIndex(DataMixin, ListView):
    model = Article
    template_name = 'general/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Article.objects.filter(is_published=True).select_related('category')


class ArticleCategory(DataMixin, ListView):
    paginate_by = 3
    model = Article
    template_name = 'general/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['category_slug'])
        d_cef = self.get_user_context(title=c.cat_name,
                                      cat_selected=c.pk)
        return dict(list(context.items()) + list(d_cef.items()))

    def get_queryset(self):
        return Article.objects.filter(category__slug=self.kwargs['category_slug'], is_published=True).select_related(
            'category')


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
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление статьи')
        return dict(list(context.items()) + list(c_def.items()))


class ContactView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'general/contact.html'
    success_url = reverse_lazy('general')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Обратная связь")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('general')

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'general/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('general')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'general/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))


def logout_user(request):
    logout(request)
    return redirect('login')


class AboutPage(DataMixin, ListView):
    model = Article
    template_name = 'general/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='О сайте')
        return dict(list(context.items()) + list(c_def.items()))


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Данной страницы не существует.</h1>'
                                'Ошибка 404.')
