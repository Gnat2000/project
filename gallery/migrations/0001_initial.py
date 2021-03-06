# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-10 18:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0005_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0430\u043b\u044c\u0431\u043e\u043c\u0430')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u0434\u043b\u044f \u0430\u043b\u044c\u0431\u043e\u043c\u0430')),
                ('img', models.ImageField(help_text='\u0420\u0430\u0437\u043c\u0435\u0440 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f 200px \u043d\u0430 200px', upload_to='image/album', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0430\u043b\u044c\u0431\u043e\u043c\u0430')),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': '\u0410\u043b\u044c\u0431\u043e\u043c',
                'verbose_name_plural': '\u0410\u043b\u044c\u0431\u043e\u043c\u044b',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0438')),
                ('img', models.ImageField(help_text='\u0416\u0435\u043b\u0430\u0442\u0435\u043b\u044c\u043d\u043e, \u0447\u0442\u043e\u0431 \u0444\u043e\u0442\u043e \u0431\u044b\u043b\u043e \u043d\u0435 \u0431\u043e\u043b\u044c\u0448\u043e\u0433\u043e \u0440\u0430\u0437\u043c\u0435\u0440\u0430', upload_to='image/photo', verbose_name='\u0424\u043e\u0442\u043e')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.Album', verbose_name='\u0410\u043b\u044c\u0431\u043e\u043c')),
                ('blog_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.BlogPost')),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': '\u0424\u043e\u0442\u043e',
                'verbose_name_plural': '\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0438',
            },
        ),
    ]
