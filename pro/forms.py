from django import forms
from .models import Project, Profile


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user','profile','posted_on']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
