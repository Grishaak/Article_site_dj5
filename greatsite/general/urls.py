from django.urls import path, re_path
from general.views import *
urlpatterns = [
    path('', index, name='general'),
    path('categories/<slug:categories_slug>/', categories),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
    path('about', about, name='about'),
]