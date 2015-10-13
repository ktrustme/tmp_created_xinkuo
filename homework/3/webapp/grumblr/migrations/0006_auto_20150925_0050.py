# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('grumblr', '0005_auto_20150925_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grumble',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 25, 0, 50, 54, 607966), blank=True),
        ),
    ]
