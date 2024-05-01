from django.contrib import admin
from .models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'created_at')


class MusicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre', 'created_at', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'genre')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'created_at')


class VideoGameAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre', 'studio', 'created_at', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'studio')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'created_at')


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'director', 'created_at', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'director')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'created_at')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'cat_name')
    list_display_links = ('id', 'cat_name')
    search_fields = ('cat_name',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Music, MusicAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(VideoGame, VideoGameAdmin)
admin.site.register(Category, CategoryAdmin)
