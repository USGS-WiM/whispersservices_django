# Generated by Django 2.1.3 on 2019-02-27 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whispersservices', '0032_auto_20181205_1856'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='eventorganization',
            unique_together={('event', 'organization')},
        ),
    ]