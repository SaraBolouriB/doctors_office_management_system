# Generated by Django 3.1.7 on 2021-03-23 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0007_auto_20210322_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='working_time',
            name='day',
            field=models.CharField(choices=[('Sat.', 'Saturday'), ('Sun.', 'Sunday'), ('Mon.', 'Monday'), ('Tue.', 'Tuesday'), ('Wed.', 'Wednesday'), ('Thu.', 'Thursday'), ('Fri.', 'Friday')], max_length=4),
        ),
    ]
