from django.db import models


class Music(models.Model):
    music_author = models.CharField(max_length=50, verbose_name='author')
    music_name = models.CharField(max_length=100, verbose_name='name')
    music_album = models.CharField(max_length=100, verbose_name='album')


class UserInfos(models.Model):
    user_type_choices = (
        (1, 'normal'),
        (2, 'VIP'),
        (3, 'SVIP'),
    )

    user_type = models.IntegerField(choices=user_type_choices)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=30)


class UserToken(models.Model):
    user = models.OneToOneField(to='UserInfos', on_delete=models.CASCADE)
    token = models.CharField(max_length=64)
