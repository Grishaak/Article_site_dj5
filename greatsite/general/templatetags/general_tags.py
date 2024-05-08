from django import template
from django.http import Http404
from general.models import *

register = template.Library()


@register.simple_tag(name='get_cats')
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)


@register.inclusion_tag('general/tagtemplates/list_posts.html')
def get_all_posts(index=True, cat_selected=0, is_posted=True):
    if index:
        # if is_posted:
        posts = Article.objects.filter(is_published=is_posted)
    else:
        posts = (Article.objects.filter(category=cat_selected)
                 .filter(is_published=is_posted))
    return {'posts': posts, 'cat_selected': cat_selected}


@register.inclusion_tag('general/tagtemplates/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.all().order_by(sort)
    return {'cats': cats, 'cat_selected': cat_selected}
