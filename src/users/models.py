# ----------------------------------------------
# users/models.py
# Models for the users app
# 
# <diogopinto> 2025+
# ----------------------------------------------



# EN:

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    # EN: ImageField - Avatar
    avatar = models.ImageField(
        upload_to='avatars/', 
        null=True, 
        blank=True,
        verbose_name='Avatar'
    )
    
    def __str__(self):
        return self.username 