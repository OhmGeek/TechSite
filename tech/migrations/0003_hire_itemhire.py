# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-25 21:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0002_auto_20170425_2130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_name', models.CharField(max_length=250)),
                ('hirer_name', models.CharField(max_length=100)),
                ('invoice_name', models.CharField(max_length=100)),
                ('email_address', models.EmailField(max_length=254)),
                ('date_out', models.DateTimeField()),
                ('date_in', models.DateTimeField()),
                ('contact_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ItemHire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tech.Hire')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tech.TechItem')),
            ],
        ),
    ]
