# Generated by Django 3.0.5 on 2020-04-18 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsinfo',
            name='news_title',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='健身资讯标题'),
        ),
        migrations.AlterField(
            model_name='newsinfo',
            name='news_type',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='类型'),
        ),
    ]