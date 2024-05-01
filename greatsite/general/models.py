from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Статья по теме'
        verbose_name_plural = 'Статьи по теме'
        ordering = ['-created_at', 'title', 'category']


class Music(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=70)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Музыка'
        verbose_name_plural = 'Музыка'


class VideoGame(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=70)
    studio = models.CharField(max_length=70)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Видео-игра'
        verbose_name_plural = 'Видео-игры'


class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=70)
    director = models.CharField(max_length=70)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class Category(models.Model):
    cat_name = models.CharField(max_length=100, db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']

    def __str__(self):
        return self.cat_name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})
