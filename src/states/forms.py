# ----------------------------------------------
# states/forms.py
# Forms for the projects app
# 
# <diogopinto> 2025+
# ----------------------------------------------

from django import forms
from .models import State

class StateForm(forms.ModelForm):

    class Meta:
        model = State
        fields = ["name", "description"]