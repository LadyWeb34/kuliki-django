from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.text import Truncator
from .models import History

# Register your models here.
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_title', 'display_image', 'status')
    def short_title(self, obj):
        return Truncator(obj.text).chars(60)  # Ограничение до 50 символов

    short_title.short_description = 'История'  # Название колонки в административной панели
    def display_image(self, obj):
        return mark_safe('<img src="{}" width="50" height="50" />'.format(obj.img.url))

    display_image.short_description = 'Изображение'  # Название колонки в административной панели
admin.site.register(History,HistoryAdmin)