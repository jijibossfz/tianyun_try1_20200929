# Generated by Django 2.2.1 on 2020-09-09 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0008_targetdistribution_drug_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoDrug2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('molregno', models.TextField(blank=True, null=True)),
                ('pref_name', models.TextField(blank=True, null=True)),
                ('chembl_id', models.TextField(blank=True, null=True)),
                ('max_phase', models.TextField(blank=True, null=True)),
                ('usan_stem_definition', models.TextField(blank=True, null=True)),
                ('indication_class', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'info_drug2',
            },
        ),
    ]
