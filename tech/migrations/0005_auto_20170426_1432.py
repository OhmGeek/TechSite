# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-26 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0004_techitem_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='techitem',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='uploads/'),
        ),
    ]