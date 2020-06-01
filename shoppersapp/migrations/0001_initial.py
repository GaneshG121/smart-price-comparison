# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScraperItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.CharField(max_length=32)),
                ('date', models.CharField(max_length=32)),
                ('image', models.CharField(max_length=344)),
                ('link', models.CharField(max_length=624)),
                ('link2', models.CharField(max_length=624)),
                ('link3', models.CharField(max_length=624)),
                ('title', models.CharField(max_length=624)),
                ('description', models.CharField(max_length=322)),
                ('days1', models.CharField(max_length=322)),
                ('days2', models.CharField(max_length=322)),
                ('days3', models.CharField(max_length=322)),
                ('location', models.CharField(max_length=32)),
                ('price', models.CharField(max_length=32)),
                ('price2', models.CharField(max_length=32)),
                ('price3', models.CharField(max_length=32)),
                ('category', models.CharField(max_length=32)),
            ],
        ),

    ]

'''class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classifications',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.CharField(max_length=32)),
                ('date', models.CharField(max_length=32)),
                ('image', models.CharField(max_length=344)),
                ('link', models.CharField(max_length=624)),
                ('link2', models.CharField(max_length=624)),
                ('link3', models.CharField(max_length=624)),
                ('title', models.CharField(max_length=2155)),
                ('description', models.CharField(max_length=322)),
                ('location', models.CharField(max_length=32)),
                ('price', models.CharField(max_length=32)),
                ('price2', models.CharField(max_length=32)),
                ('price3', models.CharField(max_length=32)),
                (' ram' ,models.CharField(max_length=644)),
                ('storage',models.CharField(max_length=624)),
                #('dispaly',models.CharField(max_length=20)),
                ('os ',models.CharField(max_length=644)),
                ('color', models.CharField(max_length=624)),
                ('camera ', models.CharField(max_length=20)),
                ('sim', models.CharField(max_length=624)),
                ('network',  models.CharField(max_length=32)),
               # (' warenty',  models.CharField(max_length=624)),
                (' battery ', models.CharField(max_length=32)),
                ('price', models.CharField(max_length=32)),
                ('category', models.CharField(max_length=32)),
            ],
        ),
     ]'''
