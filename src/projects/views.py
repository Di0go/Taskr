# ----------------------------------------------
# projects/views.py
# Views for the projects app
# 
# <diogopinto> 2025+
# ----------------------------------------------

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm



# EN: Decorator for views that checks that the user is logged in, redirecting to the log-in page if necessary as defined in te 'settings.py'
@login_required
def index(request):

    current_user = request.user

    # EN: List for all the projects the user is an onwer of
    #current_user_projects_list = Project.objects.filter(owner=current_user)

    # EN: List for all the projects the user is a member of
    current_user_projects_list = Project.objects.filter(members=current_user)
    context = {"current_user_projects_list" : current_user_projects_list}

    return render(request, "projects/projects.html", context)



# EN: This view is what the user will see when clicking a project, project details view
@login_required
def detail(request, project_id):

    project = Project.objects.get(pk=project_id)

    # TODO: Verificar se o utilizador é dono/membro do projeto, caso contrário, mandar para o 404
    return render(request, "projects/detail.html", {"project": project})



# EN: View to serve the create project form to the user
@login_required
def create_project(request):

    if request.method == "POST":
        form = ProjectForm(request.POST)

        if form.is_valid():
            project = form.save(commit=False)

            # EN: Add the user that's creating the project as the owner and member
            project.owner = request.user
            project.save()
            project.members.add(request.user)

            return redirect("projects:index")
    else:
        form = ProjectForm()

    return render(request, "projects/create_project.html", {"form": form})



# EN: View that is triggered when a user wants to delete a project
@login_required
def delete_project(request, project_id):

    # EN: Only get the project if the user is the owner of the project
    project = get_object_or_404(Project, pk=project_id, owner=request.user)

    if request.method == "POST":
        project.delete()

    return redirect("projects:index")



# EN: View that is triggered when a user wants to leave a project
@login_required
def leave_project(request, project_id):

    # EN: Only get the project if the user is a member
    project = get_object_or_404(Project, pk=project_id, members=request.user)

    if request.method == "POST":
        project.members.remove(request.user)

    return redirect("projects:index")