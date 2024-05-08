from django.urls import path, re_path

# from .templatetags.general_tags import choose
from .views import *

urlpatterns = [
    path('', ArticleIndex.as_view(), name='general'),
    path('about', about, name='about'),
    path('addarticle', ArticleAddPage.as_view(), name='add_article'),
    path('contact', contact, name='feedback'),
    path('login', login, name='login'),
    path('post/<slug:post_slug>/', ArticlePost.as_view(), name='post'),
    path('category/<slug:category_slug>/', ArticleCategory.as_view(), name='category'),
]
