# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('grumblr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grumble',
            name='photo',
            field=models.ImageField(default=b'/doge.jpg', upload_to=b'documents/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='grumble',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 24, 16, 22, 0, 645861), blank=True),
        ),
    ]
