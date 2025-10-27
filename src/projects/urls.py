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
    path("create/", views.create_project, name="create_project"),
    path("<int:project_id>/delete/", views.delete_project, name="delete_project"),
    path("<int:project_id>/leave/", views.leave_project, name="leave_project"),
    path("<int:project_id>/", views.detail, name="detail"),
]
