# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='id',
        ),
        migrations.RemoveField(
            model_name='item',
            name='todo_list',
        ),
        migrations.AlterField(
            model_name='item',
            name='title',
            field=models.CharField(max_length=100, serialize=False, primary_key=True),
        ),
        migrations.DeleteModel(
            name='List',
        ),
    ]
