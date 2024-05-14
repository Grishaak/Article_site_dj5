from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', ArticleIndex.as_view(), name='general'),
    path('about/', AboutPage.as_view(), name='about'),
    path('addarticle/', ArticleAddPage.as_view(), name='add_article'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ArticlePost.as_view(), name='post'),
    path('category/<slug:category_slug>/', ArticleCategory.as_view(), name='category'),
]
