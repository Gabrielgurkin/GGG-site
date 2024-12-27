from django.db import models


class UserInput(models.Model):
    title = models.CharField('Ввод пользователя', max_length=50)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Ввод пользователя'
        verbose_name_plural = 'Ввод пользователей'
# Create your models here.
