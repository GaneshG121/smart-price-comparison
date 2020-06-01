# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shoppersapp', '0005_auto_20190810_1333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ScraperItem',
            old_name='price',
            new_name='price1',
        ),
        migrations.AddField(
            model_name='ScraperItem',
            name='price2',
            field=models.CharField(max_length=10, default=datetime.datetime(2019, 8, 10, 8, 20, 4, 428, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ScraperItem',
            name='price3',
            field=models.CharField(max_length=10, default=datetime.datetime(2019, 8, 10, 8, 20, 4, 428, tzinfo=utc)),
            preserve_default=False,
        ),

    ]

