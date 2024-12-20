from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length= 50)
    anons = models.CharField('Анонс', max_length= 250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def _str_(self):
        return self.title


# Create your models here.
