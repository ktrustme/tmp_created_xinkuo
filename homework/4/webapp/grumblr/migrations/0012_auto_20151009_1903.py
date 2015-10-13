# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grumblr', '0011_auto_20151009_0625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='friends',
            field=models.ManyToManyField(to='grumblr.UserProfile'),
        ),
    ]
