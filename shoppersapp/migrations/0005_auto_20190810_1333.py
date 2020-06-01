# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('shoppersapp', '0004_remove_scraperitem_plus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ScraperItem',
            old_name='link',
            new_name='link1',
        ),
        migrations.AddField(
            model_name='ScraperItem',
            name='link2',
            field=models.CharField(max_length=324, default=datetime.datetime(2019, 8, 10, 8, 3, 16, 70889, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ScraperItem',
            name='link3',
            field=models.CharField(max_length=324, default=datetime.datetime(2019, 8, 10, 8, 3, 16, 70889, tzinfo=utc)),
            preserve_default=False,
        ),

    ]
