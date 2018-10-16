# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-05 09:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlackCofferData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=200)),
                ('sector', models.CharField(max_length=200)),
                ('region', models.CharField(max_length=200)),
                ('pestle', models.CharField(max_length=200)),
                ('year', models.PositiveIntegerField()),
                ('intensity', models.PositiveIntegerField()),
                ('likelihood', models.PositiveIntegerField()),
                ('relevance', models.PositiveIntegerField()),
            ],
        ),
    ]