from django import forms
from . import models

field_attrs = {'class': 'form-control'}


class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = models.Projects
        fields = ['title', 'category', 'description']
        widgets = {
            'title': forms.TextInput(attrs=field_attrs),
            'category': forms.Select(attrs=field_attrs),
            'description': forms.Textarea(attrs=field_attrs),
        }


class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Projects
        fields = ['title', 'category', 'status']
        widgets = {
            'title': forms.TextInput(attrs=field_attrs),
            'category': forms.Select(attrs=field_attrs),
            'status': forms.Select(attrs=field_attrs),
        }
