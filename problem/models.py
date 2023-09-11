from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField

# Create your models here.

class Problem(models.Model):
    title = models.CharField(max_length=256, blank=True, verbose_name='Название', help_text='Введите название для заголовка проблемы')
    slug = AutoSlugField(unique=True, populate_from='title')
    content = RichTextField(blank=True, null=True, verbose_name='Контент', help_text='Введите контент для описания проблемы')
    poster = models.ImageField(upload_to='problem/', verbose_name='Главное изображение', help_text='Загрузите изображение для записи')
    status = models.BooleanField(default=True, verbose_name='Статус', help_text='Отображает запись на странице')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проблема'
        verbose_name_plural = 'Проблемы'

class ProblemImageItem(models.Model):
    people = models.ForeignKey(Problem, blank=True, null=True, default=None, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="problem/problem_item/", verbose_name='Дополнительные изображения')
    status = models.BooleanField(default=True, verbose_name='Статус', help_text='Отображает изображение на странице')

    def __str__(self):
        return f'# = {self.id}'

    class Meta:
        verbose_name = 'Дополнительное изображение'
        verbose_name_plural = 'Дополнительные изображения'
