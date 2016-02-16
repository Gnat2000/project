# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime
from ckeditor.fields import RichTextField
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User
import mptt
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('tree_id', 'level')

    name = models.CharField(max_length=150, verbose_name='Категория')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', verbose_name='Родительский класс')

    def __unicode__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']


mptt.register(Category, order_insertion_by=['name'])


class BlogPost(models.Model):
    class Meta:
        ordering = ['title']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    title = models.CharField('Заголовок', max_length=150)
    body = RichTextField('Текст статьи')
    date = models.DateTimeField('Дата создания', default=datetime.datetime.now)
    image = models.ImageField('Изображение', upload_to='image', blank=True,
                              help_text='Размер изображения 250px на 300px')
    slug = models.SlugField()
    likes = models.IntegerField(default=0)
    video = EmbedVideoField(null=True, blank=True, verbose_name='Видео')
    category = TreeForeignKey(Category, blank=True, null=True, related_name='cat')

    def __unicode__(self):
        return self.title

    # Preview "image" in Administration Interface
    def preview(self):
        if self.image:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="50"/></a>'.format(self.image.url)
        else:
            return '(Нет изображения)'

    preview.short_description = 'Изображение'
    preview.allow_tags = True


class Comment(models.Model):
    class Meta:
        db_table = 'comment'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    comments_text = models.TextField(verbose_name='Текст комментария')
    comments_blog = models.ForeignKey(BlogPost)
    comments_date = models.DateField(auto_now=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True)

    def __unicode__(self):
        return self.comments_text
