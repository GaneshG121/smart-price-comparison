# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppersapp', '0011_scraperitem_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ScraperItem',
            name='title1',
        ),
    ]

