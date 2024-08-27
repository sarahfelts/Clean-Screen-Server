from django import forms
from cleanscreenapi.models import WarningIterable

class WarningForm(forms.ModelForm):
    class Meta:
        model = WarningIterable
        fields = ('timestamp', 'description', 'tag', 'severity', 'approved', 'movie', 'user')
