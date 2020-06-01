# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations



class Migration(migrations.Migration):

    dependencies = [
        ('shoppersapp', '0012_remove_scraperitem_title1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ScraperItem',
            name='price2',
            field=models.CharField(max_length=32),
        ),
    ]
