# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-12 12:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coupdeg', '0011_cart_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='item',
            name='content_type',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
