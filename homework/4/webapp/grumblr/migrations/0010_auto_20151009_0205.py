# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grumblr', '0009_auto_20151009_0204'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='introduction',
            field=models.TextField(default=b"This layzy guy didn't say anything.", max_length=420),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='saying',
            field=models.TextField(default=b'My Heart Is In The Work!'),
        ),
    ]
