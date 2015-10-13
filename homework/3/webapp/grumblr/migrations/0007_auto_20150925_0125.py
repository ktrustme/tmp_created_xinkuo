# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grumblr', '0006_auto_20150925_0050'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='saying',
            field=models.TextField(default=b'My Heart Is In The Work!'),
        ),
        migrations.AlterField(
            model_name='grumble',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
