from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class People(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя человека", help_text="Введите полностью ФИО человека", blank=True)
    text = models.TextField(verbose_name='Текст контента', help_text='Введите текст, который будет отображаться на странице с записью', blank=True)
    poster = models.ImageField(upload_to='people/', verbose_name='Главное изображение', help_text='Загрузите изображение для записи')
    status = models.BooleanField(default=True, verbose_name='Статус', help_text='Отображает запись на странице')
    slug = AutoSlugField(populate_from='name', unique=True, null=True, default=None)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Люди'
        verbose_name_plural = 'Люди'

class PeopleImageList(models.Model):
    people = models.ForeignKey(People, blank=True, null=True, default=None, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="people/people_list/", verbose_name='Дополнительные изображения')
    status = models.BooleanField(default=True, verbose_name='Статус', help_text='Отображает изображение на странице')

    def __str__(self):
        return f'Id = {self.id}'

    class Meta:
        verbose_name = 'Дополнительное изображение'
        verbose_name_plural = 'Дополнительные изображения'