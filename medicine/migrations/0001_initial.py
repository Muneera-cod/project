# Generated by Django 3.2.23 on 2024-04-07 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('medicine_id', models.AutoField(primary_key=True, serialize=False)),
                ('med_name', models.CharField(max_length=45)),
                ('price', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'medicine',
                'managed': False,
            },
        ),
    ]
