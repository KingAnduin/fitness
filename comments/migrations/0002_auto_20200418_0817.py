# Generated by Django 3.0.5 on 2020-04-18 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='CommentsInfo',
            name='good_id',
        ),
        migrations.RemoveField(
            model_name='CommentsInfo',
            name='user_account',
        ),
    ]
