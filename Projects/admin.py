from django.contrib import admin
from django.db.models import Count
from . import models

admin.site.register(models.Category)


@admin.register(models.Projects)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'user', 'category', 'created_Date', 'tasks_count']
    list_per_page = 10
    list_select_related = ['user', 'category']
    list_editable = ['status']

    def tasks_count(self, obj):
        return obj.tasks_count

    def get_queryset(self, request):
        query = super().get_queryset(request)
        query = query.annotate(tasks_count=Count('task'))
        return query


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'project', 'is_completed']
    list_per_page = 10
    list_editable = ['is_completed']