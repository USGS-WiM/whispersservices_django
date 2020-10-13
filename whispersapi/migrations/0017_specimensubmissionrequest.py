# Generated by Django 2.1 on 2018-10-11 21:23

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('whispersapi', '0016_specimensubmissionrequestresponse_specimensubmissionrequesttype'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecimenSubmissionRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(blank=True, db_index=True, default=datetime.date.today, null=True)),
                ('modified_date', models.DateField(auto_now=True, null=True)),
                ('request_datetime', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='specimensubmissionrequest_creator', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='specimensubmissionrequest_modifier', to=settings.AUTH_USER_MODEL)),
                ('request_response', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='whispersapi.SpecimenSubmissionRequestResponse')),
                ('request_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='whispersapi.SpecimenSubmissionRequestType')),
                ('response_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='specimensubmissionrequests_responder', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'whispers_specimensubmissionrequest',
            },
        ),
    ]