# Generated by Django 3.2.23 on 2024-04-07 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('prescription_id', models.AutoField(primary_key=True, serialize=False)),
                ('prescription', models.CharField(max_length=450)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
            options={
                'db_table': 'prescription',
                'managed': False,
            },
        ),
    ]
