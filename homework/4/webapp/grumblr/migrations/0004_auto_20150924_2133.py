# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('grumblr', '0003_auto_20150924_2109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='url',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='firstname',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='lastname',
            field=models.TextField(default=b''),
        ),
        migrations.AlterField(
            model_name='grumble',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 24, 21, 33, 58, 383914), blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.TextField(default=b'Unknown'),
        ),
    ]
