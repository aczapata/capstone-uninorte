# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-28 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20160328_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FileField(upload_to='projects'),
        ),
    ]
