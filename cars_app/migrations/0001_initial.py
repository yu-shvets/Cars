# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-09 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=256)),
                ('model', models.CharField(max_length=256)),
                ('age', models.PositiveIntegerField()),
                ('color', models.CharField(max_length=256)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-datetime'],
                'verbose_name_plural': 'Cars',
                'verbose_name': 'Car',
            },
        ),
    ]
