# Generated by Django 2.2.1 on 2020-09-29 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_advice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advice',
            name='advice',
            field=models.TextField(max_length=100, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='advice',
            name='name',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='advice',
            name='phone',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='email'),
        ),
    ]