# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppersapp', '0008_scraperitem_title1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ScraperItem',
            name='description',
            field=models.CharField(max_length=31122),
        ),
        migrations.AlterField(
            model_name='ScraperItem',
            name='days1',
            field=models.CharField(max_length=31122),
        ),
        migrations.AlterField(
            model_name='ScraperItem',
            name='days2',
            field=models.CharField(max_length=31122),
        ),
        migrations.AlterField(
            model_name='ScraperItem',
            name='days3',
            field=models.CharField(max_length=31122),
        ),
        migrations.AlterField(
            model_name='ScraperItem',
            name='image',
            field=models.CharField(max_length=644),
        ),
        migrations.AlterField(
            model_name='ScraperItem',
            name='link1',
            field=models.CharField(max_length=624),
        ),
        migrations.AlterField(
            model_name='ScraperItem',
            name='link2',
            field=models.CharField(max_length=624),
        ),
        migrations.AlterField(
            model_name='ScraperItem',
            name='link3',
            field=models.CharField(max_length=624),
        ),
        migrations.AlterField(
            model_name='ScraperItem',
            name='price1',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='ScraperItem',
            name='title1',
            field=models.CharField(max_length=624),
        ),
    ]
