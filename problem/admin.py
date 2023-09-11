from django.contrib import admin
from .models import Problem, ProblemImageItem
# Register your models here.

class ProblemImageInline(admin.TabularInline):
    model = ProblemImageItem
    extra = 0

class ProblemAdmin(admin.ModelAdmin):
    inlines = [ProblemImageInline]
    list_display = ('title', 'slug')
    class Meta:
        model = Problem

admin.site.register(Problem, ProblemAdmin)