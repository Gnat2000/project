# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-07 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160207_0010'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['title'], 'verbose_name': '\u0421\u0442\u0430\u0442\u044c\u044f', 'verbose_name_plural': '\u0421\u0442\u0430\u0442\u044c\u0438'},
        ),
        migrations.AddField(
            model_name='blogpost',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
