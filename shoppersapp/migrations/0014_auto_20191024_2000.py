# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppersapp', '0013_auto_20190813_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scraperitem',
            name='days1',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='scraperitem',
            name='days2',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='scraperitem',
            name='days3',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='scraperitem',
            name='description',
            field=models.CharField(max_length=6122),
        ),
        migrations.AlterField(
            model_name='scraperitem',
            name='image',
            field=models.CharField(max_length=624),
        ),
    ]
