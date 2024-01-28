from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    PRIORITY_CHOICES = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]

    priority = forms.ChoiceField(choices=PRIORITY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'due', 'priority', 'category']
        widgets = {
            'due': forms.DateInput(attrs={'type': 'date'}),
        }
