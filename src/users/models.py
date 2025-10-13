# ----------------------------------------------
# users/models.py
# Models for the users app
# 
# <diogopinto> 2025+
# ----------------------------------------------

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.db import models


# EN: Validate file size (file, max size in MB)
def validate_file_size(l_file, max_file_size):
    max_size_mb = max_file_size * 1024 * 1024

    if l_file.size > max_size_mb:
        raise ValidationError(f"The image size shouldn't exceed {max_size_mb} MB")

class CustomUser(AbstractUser):

    # EN: ImageField - Avatar
    avatar = models.ImageField(
        upload_to='users/avatars/', 
        null=True, 
        blank=True,
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
            lambda this: validate_file_size(this, 1),
        ],
        verbose_name='Avatar'
    )
    
    def __str__(self):
        return self.username 