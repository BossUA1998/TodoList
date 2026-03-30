from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]
        widgets = {
            "tags": forms.CheckboxSelectMultiple,
            "deadline": forms.DateInput(attrs={"type": "date"}),
        }


class TaskSearchForm(forms.Form):
    content = forms.CharField(max_length=256)
