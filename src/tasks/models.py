from django.db import models
from django.conf import settings
from projects.models import Project
from states.models import State

class Task(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)

    # --- data limite e prioridade ---
    due_date = models.DateField(null=True, blank=True)

    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    ]
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default="medium")

    # --- datas automáticas ---
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks")
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="tasks")

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="created_tasks"
    )

    # ordem dentro de cada coluna
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["state__order", "order", "-updated_at"]

    def __str__(self):
        return self.title
