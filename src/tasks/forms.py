from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "due_date", "priority", "assigned_to"]
        widgets = {
        "due_date": forms.DateInput(attrs={"type": "date"}),
}
          
    def __init__(self, *args, project=None, **kwargs):
        super().__init__(*args, **kwargs)
        if project is not None:
            self.fields["assigned_to"].queryset = project.members.all()

class TaskMoveForm(forms.Form):
    state_id = forms.IntegerField()
    new_order = forms.IntegerField(required=False)
