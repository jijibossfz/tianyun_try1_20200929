# Generated by Django 2.2.1 on 2020-09-02 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0006_auto_20200818_0815'),
    ]

    operations = [
        migrations.AddField(
            model_name='phasedistribution',
            name='drug',
            field=models.TextField(blank=True, null=True),
        ),
    ]
