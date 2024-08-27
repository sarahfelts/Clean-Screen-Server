from django import forms
from cleanscreenapi.models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'year', 'rating', 'genre')