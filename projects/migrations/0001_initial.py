# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-28 16:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('title_en', models.CharField(max_length=255)),
                ('abstract', models.CharField(max_length=200)),
                ('abstract_en', models.CharField(max_length=200)),
                ('image', models.FileField(upload_to=b'')),
                ('advisor', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('major', models.CharField(max_length=255)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Team')),
            ],
        ),
    ]