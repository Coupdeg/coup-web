# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupdeg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to=b'')),
                ('image_types', models.CharField(choices=[(b'0', b'user'), (b'1', b'product')], max_length=1)),
                ('type_id', models.IntegerField(blank=True)),
                ('role', models.IntegerField(default=0)),
            ],
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_type',
            new_name='product_types',
        ),
    ]
