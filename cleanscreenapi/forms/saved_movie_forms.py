from django import forms
from cleanscreenapi.models import SavedMovie

class SavedMovieForm(forms.ModelForm):
    class Meta:
        model = SavedMovie
        fields = ('movie',)
