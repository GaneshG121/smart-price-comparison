# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppersapp', '0002_auto_20160403_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='ScraperItem',
            name='plus',
            field=models.CharField(max_length=52, default=1),
            preserve_default=False,
        ),

    ]

