# Generated by Django 3.1.7 on 2021-03-21 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0003_auto_20210321_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='working_time',
            name='day',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='working_time',
            name='end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='working_time',
            name='start_time',
            field=models.TimeField(),
        ),
    ]
