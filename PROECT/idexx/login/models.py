from django.db import models


class Login(models.Model):
    log = models.CharField('Имя пользователя', max_length=30)
    pas = models.CharField('Пароль', max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'