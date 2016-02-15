from __future__ import unicode_literals
# -*- coding: utf-8 -*-
from django.db import models
from blog.models import BlogPost


class Album(models.Model):
    title = models.CharField("Название альбома", max_length=100)
    slug = models.SlugField("Ссылка для альбома", max_length=100, unique=True)
    img = models.ImageField("Изображение альбома", upload_to='image/album',
                            help_text='Размер изображения 200px на 200px')
    biography = models.OneToOneField(BlogPost, verbose_name='Биография')

    class Meta:
        ordering = ['title']
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'

    def __unicode__(self):
        return self.title


class Photo(models.Model):
    title = models.CharField("Название фотографии", max_length=100)
    album = models.ForeignKey(Album, verbose_name='Альбом')
    blog_post = models.ForeignKey(BlogPost)
    img = models.ImageField("Фото", upload_to='image/photo',
                            help_text='Желательно, чтоб фото было не большого размера')

    class Meta:
        ordering = ['title']
        verbose_name = 'Фото'
        verbose_name_plural = "Фотографии"

    def __unicode__(self):
        return self.title
