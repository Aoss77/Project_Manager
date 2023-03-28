from django import forms
from . import models

field_attrs = {'class': 'form-control mb-2'}


class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = models.Projects
        fields = ['title', 'category', 'description']
        widgets = {
            'title': forms.TextInput(),
            'category': forms.Select(),
            'description': forms.Textarea(),
        }


class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Projects
        fields = ['title', 'category', 'status']
        widgets = {
            'title': forms.TextInput(),
            'category': forms.Select(),
            'status': forms.Select(),
        }
