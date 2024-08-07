# Generated by Django 3.2.23 on 2024-04-07 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('age', models.CharField(max_length=45)),
                ('gender', models.CharField(max_length=45)),
                ('place', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
                ('phone_no', models.CharField(max_length=45)),
                ('username', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'user_reg',
                'managed': False,
            },
        ),
    ]
