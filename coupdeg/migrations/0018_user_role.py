# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-15 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupdeg', '0017_auto_20171115_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[(b'0', b'user'), (b'1', b'admin')], default=0, max_length=1),
        ),
    ]