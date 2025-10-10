# ----------------------------------------------
# projects/urls.py
# URL Mappings for the projects app.
# 
# <diogopinto> 2025+
# ----------------------------------------------

from django.urls import path
from . import views

app_name = "projects"

urlpatterns = [
    # EN: /projects/ will lead here
    path("", views.index, name="index"),

]
