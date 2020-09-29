# Generated by Django 2.2.1 on 2020-08-09 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0004_clinicaldetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clinicalbrowse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_id', models.TextField(blank=True, null=True)),
                ('public_title', models.TextField(blank=True, null=True)),
                ('date_of_registration', models.TextField(blank=True, null=True)),
                ('recruitment_status', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'clinical_browse',
            },
        ),
    ]
