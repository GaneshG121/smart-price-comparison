# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppersapp', '0009_auto_20190813_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scraperitem',
            name='description',
            field=models.CharField(max_length=61122),
        ),
    ]
