from django import forms
from .models import Task


class TaskForm(forms.Form):
    """Form for creating and updating tasks"""
    
    description = forms.CharField(
        label='Description',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Enter task description'
        }),
        max_length=300
    )
    
    owner = forms.CharField(
        label='Owner',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter task owner name'
        }),
        max_length=100
    )
    
    deadline = forms.DateField(
        label='Deadline',
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )
    
    status = forms.ChoiceField(
        label='Status',
        choices=Task.STATUS_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )

    def save_task(self, task=None):
        """Save form data to Task document"""
        if task is None:
            task = Task()
        
        task.description = self.cleaned_data['description']
        task.owner = self.cleaned_data['owner']
        task.deadline = self.cleaned_data['deadline']
        task.status = self.cleaned_data['status']
        task.save()
        return task
