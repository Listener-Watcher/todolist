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
                ('title', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('text', models.TextField()),
                ('createdTime', models.DateTimeField()),
                ('priority', models.IntegerField(default=1, choices=[(0, b'Urgent'), (1, b'Normal')])),
                ('finished', models.IntegerField(default=0, choices=[(0, b'Unfinished'), (1, b'finished')])),
            ],
            options={
                'ordering': ['-priority', 'title'],
            },
        ),
    ]
