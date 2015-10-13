# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('grumblr', '0004_auto_20150924_2133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grumble',
            name='photo',
        ),
        migrations.AlterField(
            model_name='grumble',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 25, 0, 40, 49, 670746), blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(default=b'/default_photo/sillydog.jpg', upload_to=b'documents/%y/%m/%d'),
        ),
    ]
