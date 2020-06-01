# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppersapp', '0010_auto_20190813_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='ScraperItem',
            name='price',
            field=models.CharField(max_length=32, default=2),
            preserve_default=False,
        ),
    ]


