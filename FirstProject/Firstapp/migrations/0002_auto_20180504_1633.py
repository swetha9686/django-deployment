# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-04 11:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Firstapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]