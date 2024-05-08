# Generated by Django 5.0.4 on 2024-05-05 17:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='general.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(blank=True, verbose_name='Контент'),
        ),
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Создано'),
        ),
        migrations.AlterField(
            model_name='article',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='article',
            name='photo',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='article',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Обновлено'),
        ),
    ]
