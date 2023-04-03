from django.db import models


class Tasks(models.Model):
    title = models.CharField('Номер главы', max_length=30)
    intro = models.CharField('О главе', max_length=250)
    full_text = models.TextField('Обучение')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
