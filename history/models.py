from django.db import models

# Create your models here.
class History(models.Model):
    text = models.TextField( verbose_name='Заголовок', help_text='Введите заголовок поста', blank=True)
    img = models.ImageField(upload_to='history/', verbose_name='Изображение', help_text='Загрузите изображение для записи')
    status = models.BooleanField(default=True, verbose_name='Статус', help_text='Отображает запись на странице')

    def __str__(self):
        return "Запись - %s..." % (self.text[:50])

    class Meta:
        verbose_name = 'История'
        verbose_name_plural = 'Истории'