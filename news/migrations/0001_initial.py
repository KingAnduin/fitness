# Generated by Django 3.0.5 on 2020-04-18 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(max_length=50, verbose_name='健身资讯标题')),
                ('news_type', models.CharField(max_length=50, verbose_name='类型')),
                ('news_level', models.CharField(blank=True, max_length=50, null=True, verbose_name='级别')),
                ('news_major_muscle', models.CharField(blank=True, max_length=50, null=True, verbose_name='主要肌肉群')),
                ('news_other_muscle', models.CharField(blank=True, max_length=50, null=True, verbose_name='其他肌肉')),
                ('news_equipment', models.CharField(blank=True, max_length=50, null=True, verbose_name='器械要求')),
                ('news_gif', models.CharField(blank=True, max_length=200, null=True, verbose_name='gif')),
                ('news_image', models.CharField(blank=True, max_length=200, null=True, verbose_name='预览图')),
                ('news_url', models.CharField(max_length=200, verbose_name='网址')),
            ],
        ),
    ]