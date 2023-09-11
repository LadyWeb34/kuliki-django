from django.contrib import admin
from .models import People, PeopleImageList

# Register your models here.
class PeopleImageInline(admin.TabularInline):
    model = PeopleImageList
    extra = 0

class PeopleAdmin(admin.ModelAdmin):
    inlines = [PeopleImageInline]
    class Meta:
        model = People

admin.site.register(People, PeopleAdmin)