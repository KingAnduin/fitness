# Generated by Django 3.0.5 on 2020-04-25 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('good', '0004_auto_20200417_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='good_image',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='商品图片'),
        ),
    ]
