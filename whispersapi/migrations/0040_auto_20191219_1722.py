# Generated by Django 2.2.4 on 2019-12-19 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whispersapi', '0039_auto_20191126_1228'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='notificationcuestandard',
            unique_together={('notification_cue_preference', 'standard_type', 'created_by')},
        ),
    ]
