from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Max

from .models import Task
from .forms import TaskForm, TaskMoveForm
from projects.models import Project
from states.models import State


def _get_project_for_member(project_id, user):
    # segue o vosso padrão: membros do projeto
    return get_object_or_404(Project, id=project_id, members=user)


@login_required
def create_task(request, project_id, state_id):
    project = _get_project_for_member(project_id, request.user)
    state = get_object_or_404(State, id=state_id, project=project)

    if request.method == "POST":
        form = TaskForm(request.POST, project=project)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.state = state
            task.created_by = request.user

            max_order = Task.objects.filter(state=state).aggregate(Max("order"))["order__max"]
            task.order = (max_order + 1) if max_order is not None else 0

            task.save()
    return redirect("projects:detail", project_id=project.id)


@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, project__members=request.user)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task, project=task.project)
        if form.is_valid():
            form.save()
    return redirect("projects:detail", project_id=task.project.id)


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, project__members=request.user)

    project_id = task.project.id
    state = task.state
    deleted_order = task.order
    task.delete()

    # fechar o “buraco” na ordem da coluna
    for t in Task.objects.filter(state=state, order__gt=deleted_order).order_by("order"):
        t.order -= 1
        t.save(update_fields=["order"])

    return redirect("projects:detail", project_id=project_id)


@login_required
def move_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, project__members=request.user)

    if request.method != "POST":
        return redirect("projects:detail", project_id=task.project.id)

    form = TaskMoveForm(request.POST)
    if not form.is_valid():
        return redirect("projects:detail", project_id=task.project.id)

    project = task.project
    new_state = get_object_or_404(State, id=form.cleaned_data["state_id"], project=project)

    old_state = task.state
    old_order = task.order

    # 1) fechar buraco na coluna antiga
    for t in Task.objects.filter(state=old_state, order__gt=old_order).order_by("order"):
        t.order -= 1
        t.save(update_fields=["order"])

    # 2) calcular posição na nova coluna
    new_order = form.cleaned_data.get("new_order")
    if new_order is None:
        max_order = Task.objects.filter(state=new_state).aggregate(Max("order"))["order__max"]
        new_order = (max_order + 1) if max_order is not None else 0
    else:
        # empurrar para baixo quem já está a partir dessa posição
        for t in Task.objects.filter(state=new_state, order__gte=new_order).order_by("-order"):
            t.order += 1
            t.save(update_fields=["order"])

    task.state = new_state
    task.order = new_order
    task.save(update_fields=["state", "order"])

    return redirect("projects:detail", project_id=project.id)
