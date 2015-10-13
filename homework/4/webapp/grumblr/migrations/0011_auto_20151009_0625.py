# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grumblr', '0010_auto_20151009_0205'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='friends',
            field=models.ManyToManyField(related_name='friends_rel_+', to='grumblr.UserProfile'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='introduction',
            field=models.TextField(default=b"This lazy guy didn't say anything.", max_length=420),
        ),
    ]
