# ----------------------------------------------
# users/views.py
# Views for the users app
# 
# <diogopinto> 2025+
# ----------------------------------------------

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    # EN: Form to use with this view
    form_class = CustomUserCreationForm

    # EN: Redirect to login after registration
    success_url = reverse_lazy('users:login')

    template_name = 'users/register.html'