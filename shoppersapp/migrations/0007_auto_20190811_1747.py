# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppersapp', '0006_auto_20190810_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ScraperItem',
            name='link1',
            field=models.CharField(max_length=324),
        ),
        migrations.AlterField(
            model_name='ScraperItem',
            name='price3',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='ScraperItem',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
