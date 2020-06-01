# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppersapp', '0007_auto_20190811_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='ScraperItem',
            name='title1',
            field=models.CharField(max_length=324, default=2),
            preserve_default=False,
        ),
    ]
