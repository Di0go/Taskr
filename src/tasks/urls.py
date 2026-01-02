from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    path("create/<int:project_id>/<int:state_id>/", views.create_task, name="create"),
    path("edit/<int:task_id>/", views.edit_task, name="edit"),
    path("delete/<int:task_id>/", views.delete_task, name="delete"),
    path("move/<int:task_id>/", views.move_task, name="move"),
]
