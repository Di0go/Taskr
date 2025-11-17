# ----------------------------------------------
# states/urls.py
# URL Mappings for the states app.
# 
# <diogopinto> 2025+
# ----------------------------------------------

from django.urls import path
from . import views

app_name = "states"

urlpatterns = [
    path("create/<int:project_id>/", views.create_state, name="create_state"),
    path("delete/<int:state_id>/", views.delete_state, name="delete_state"),
]
