# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppersapp', '0003_scraperitem_plus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ScraperItem',
            name='plus',
        ),
    ]

