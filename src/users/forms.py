# ----------------------------------------------
# users/forms.py
# Forms for the users apo
# 
# <diogopinto> 2025+
# ----------------------------------------------

from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

# EN: This extends the UserCreationForm to add the avatar field
class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('avatar',)
