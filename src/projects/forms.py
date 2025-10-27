# ----------------------------------------------
# projects/forms.py
# Forms for the projects app
# 
# <diogopinto> 2025+
# ----------------------------------------------

from django import forms
from .models import Project

# EN: This extends the UserCreationForm to add the avatar field
class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ["name", "description"]