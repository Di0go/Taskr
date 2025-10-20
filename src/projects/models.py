# ----------------------------------------------
# projects/models.py
# Models for the projects app
# 
# <diogopinto> 2025+
# ----------------------------------------------

from django.db import models
from users.models import CustomUser

class Project(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    # EN: related_name solves the reverse accessor clash issue
    members = models.ManyToManyField(CustomUser, related_name="members")