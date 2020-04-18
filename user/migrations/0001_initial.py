# Generated by Django 3.0.5 on 2020-04-16 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11, verbose_name='电话')),
                ('password', models.CharField(max_length=16, verbose_name='密码')),
            ],
            options={
                'verbose_name': '用户账户',
            },
        ),
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=64)),
                ('user_account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.UserAccount')),
            ],
            options={
                'verbose_name': '用户token',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名字')),
                ('nickname', models.CharField(blank=True, max_length=10, null=True, verbose_name='昵称')),
                ('sex', models.CharField(blank=True, max_length=1, null=True, verbose_name='性别')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='生日')),
                ('head_image', models.CharField(blank=True, max_length=255, null=True, verbose_name='头像')),
                ('contact_phone', models.CharField(blank=True, max_length=11, null=True, verbose_name='联系人电话')),
                ('user_account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.UserAccount')),
            ],
            options={
                'verbose_name': '用户信息',
            },
        ),
    ]
