# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('createdTime', models.DateTimeField()),
                ('priority', models.IntegerField(default=1, choices=[(0, b'Urgent'), (1, b'Normal')])),
                ('finished', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-priority', 'title'],
            },
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=250)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.AddField(
            model_name='item',
            name='todo_list',
            field=models.ForeignKey(to='todolist.List'),
        ),
    ]
