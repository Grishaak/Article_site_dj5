from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'get_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'created_at')
    fields = ('title', 'slug', 'category', 'photo', 'is_published', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

    def get_photo(self, object):
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}" width=50>')

    get_photo.short_description = 'Изображение'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'cat_name')
    list_display_links = ('id', 'cat_name')
    search_fields = ('cat_name',)
    prepopulated_fields = {'slug': ('cat_name',)}


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = "Админ-панель сайта по статьям"
admin.site.site_header = "Админ-панель сайта по статьям"
