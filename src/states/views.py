# ----------------------------------------------
# states/views.py
# Views for the states app
# 
# <diogopinto> 2025+
# ----------------------------------------------

from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Max
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import State
from projects.models import Project
from .forms import StateForm



@login_required
def create_state(request, project_id):

    if request.method == "POST":
        form = StateForm(request.POST)

        if form.is_valid():
            l_state = form.save(commit=False)

            # EN: Get the max order of all of the state objects of this project
            max_order = State.objects.filter(project_id=project_id).aggregate(Max('order'))['order__max']

            l_state.order = (max_order + 1) if max_order is not None else 0
            l_state.project = get_object_or_404(Project, pk=project_id)

            l_state.save()

            return redirect("projects:detail", project_id=project_id)
    else:
        form = StateForm()

    return render(request, "states/create_state.html", {"form": form, "project_id": project_id})



# EN: View that is triggered when a user wants to delete a state
@login_required
def delete_state(request, state_id):

    # EN: Only get the project if the user is the owner of the project
    state = get_object_or_404(State, pk=state_id)
    project_id = state.project.id

    if request.method == "POST":
        state.delete()

    return redirect("projects:detail", project_id=project_id)