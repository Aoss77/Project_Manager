from django.contrib import admin
from . import models

admin.site.register(models.Category)


@admin.register(models.Projects)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'user', 'category', 'created_Date']
    list_per_page = 10


admin.site.register(models.Task)
# Register your models here.Projects
