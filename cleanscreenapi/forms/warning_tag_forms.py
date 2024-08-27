from django import forms
from cleanscreenapi.models import WarningTag

class WarningTagForm(forms.ModelForm):
    class Meta:
        model = WarningTag
        fields = ('warning', 'tag')
