# ----------------------------------------------
# states/models.py
# Models for the states app
# 
# <diogopinto> 2025+
# ----------------------------------------------

from django.db import models
from projects.models import Project

class State(models.Model):
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=200, default="")
    order = models.IntegerField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name