# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-04 15:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coupdeg', '0007_user_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name=b'date published')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coupdeg.Product')),
            ],
        ),
    ]
