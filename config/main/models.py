from django.db import models


class Login(models.Model):
    username = models.CharField(max_length=50, verbose_name='Никнейм')
    password = models.CharField(max_length=50, verbose_name='Пароль')

    def __str__(self):
        return self.username