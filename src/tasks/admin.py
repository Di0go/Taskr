from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "project", "state", "order", "created_by", "updated_at")
    list_filter = ("project", "state")
    search_fields = ("title", "description")

