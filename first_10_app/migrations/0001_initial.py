# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 23:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('name0', models.CharField(max_length=120)),
                ('name1', models.CharField(max_length=120)),
                ('name2', models.CharField(max_length=120)),
                ('name3', models.CharField(max_length=120)),
                ('name4', models.CharField(max_length=120)),
                ('name5', models.CharField(max_length=120)),
                ('name6', models.CharField(max_length=120)),
                ('name7', models.CharField(max_length=120)),
                ('name8', models.CharField(max_length=120)),
                ('name9', models.CharField(max_length=120)),
            ],
        ),
    ]