
from django.forms import ModelForm
from django import forms

from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'featured_image', 'demo_link', 'source_link', 'tags']

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    #override init

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        #self.fields['title'].widget.attrs.update({'class':'input', 'placeholder': 'Add a title'})
        #self.fields['description'].widget.attrs.update({'class':'input', 'placeholder': 'Add description'})

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})