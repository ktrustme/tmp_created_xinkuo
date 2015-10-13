# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grumblr', '0007_auto_20150925_0125'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='age',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='background',
            field=models.ImageField(default=b'/default_background/beach.jpg', upload_to=b'documents/%y/%m/%d'),
        ),
    ]
