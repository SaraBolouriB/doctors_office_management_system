# Generated by Django 3.1.7 on 2021-03-21 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='fname',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='lname',
        ),
        migrations.RemoveField(
            model_name='normal_user',
            name='fname',
        ),
        migrations.RemoveField(
            model_name='normal_user',
            name='lname',
        ),
        migrations.AddField(
            model_name='all_users',
            name='password',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='name',
            field=models.CharField(default=12, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='normal_user',
            name='name',
            field=models.CharField(default='Sara', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
