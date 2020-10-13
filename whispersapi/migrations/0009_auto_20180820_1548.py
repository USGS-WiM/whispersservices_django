# Generated by Django 2.0 on 2018-08-20 20:48

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whispersapi', '0008_auto_20180820_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='search',
            name='data',
        ),
        migrations.AddField(
            model_name='search',
            name='query_params',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=''),
            preserve_default=False,
        ),
    ]