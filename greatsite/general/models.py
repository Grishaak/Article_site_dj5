from django.db import models


class Music(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

