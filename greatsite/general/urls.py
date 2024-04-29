from django.urls import path, re_path
from general.views import *

urlpatterns = [
    path('', index, name='general'),
    path('about', about, name='about'),
    path('addarticle', add_article, name='add_article'),
    path('contact', contact, name='feedback'),
    path('login', login, name='login'),
    path('post/<int:post_id>/', show_post, name='post'),
]
