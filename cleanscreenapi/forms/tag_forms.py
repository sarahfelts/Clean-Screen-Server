from django import forms
from cleanscreenapi.models import Tag

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('name',)
