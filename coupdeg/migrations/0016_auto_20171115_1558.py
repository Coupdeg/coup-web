# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-15 08:58
from __future__ import unicode_literals

import django_imgur.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupdeg', '0015_auto_20171113_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, null=True, storage=django_imgur.storage.ImgurStorage(), upload_to=b'photos'),
        ),
    ]
