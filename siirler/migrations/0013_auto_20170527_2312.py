# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 23:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siirler', '0012_auto_20170527_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitap',
            name='slug',
            field=models.SlugField(blank=True, help_text='A label for URL config.', max_length=36, null=True),
        ),
        migrations.AlterField(
            model_name='sair',
            name='slug',
            field=models.SlugField(blank=True, help_text='A label for URL config.', max_length=63, null=True),
        ),
    ]
