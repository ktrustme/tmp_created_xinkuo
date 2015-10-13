# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('grumblr', '0002_auto_20150924_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.ImageField(default=b'/doge.jpg', upload_to=b'documents/%y/%m/%d')),
                ('background', models.ImageField(default=b'/beach.jpg', upload_to=b'documents/%y/%m/%d')),
                ('url', models.URLField()),
                ('email', models.TextField()),
                ('gender', models.TextField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='grumble',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 24, 21, 9, 43, 736598), blank=True),
        ),
    ]
