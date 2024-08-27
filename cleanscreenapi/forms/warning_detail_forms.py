from django import forms
from cleanscreenapi.models import WarningDetail

class WarningDetailForm(forms.ModelForm):
    class Meta:
        model = WarningDetail
        fields = ('name', 'tag')
