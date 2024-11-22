from django.db import models

class News_post(models.Model):
    title = models.CharField('Название новости', max_length=200)
    short_desription = models.CharField('Краткое описание', max_length=200)
    text = models.TextField('Новость')
    pub_date = models.DateTimeField('Дата публикации')
    author = models.CharField('Автор', max_length=70)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
