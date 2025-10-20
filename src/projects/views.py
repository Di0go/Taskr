# ----------------------------------------------
# projects/views.py
# Views for the projects app
# 
# <diogopinto> 2025+
# ----------------------------------------------

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Project
from users.models import CustomUser

# EN: Decorator for views that checks that the user is logged in, redirecting to the log-in page if necessary as defined in te 'settings.py'
@login_required
def index(request):

    current_user = request.user

    # EN: List for all the projects the user is the owner of
    # TODO: Also add projects that the user is a member of, to simplify everything, let's always make the owner a member and only use the owner field for permission stuff
    current_user_projects_list = Project.objects.filter(owner=current_user)
    context = {"current_user_projects_list" : current_user_projects_list}

    return render(request, "projects/projects.html", context)



# EN: This view is what the user will see when clicking a project, project details view
@login_required
def detail(request, project_id):

    project = Project.objects.get(pk=project_id)

    # TODO: Verificar se o utilizador é dono/membro do projeto, caso contrário, mandar para o 404
    return HttpResponse(f"You're in project {project}")
