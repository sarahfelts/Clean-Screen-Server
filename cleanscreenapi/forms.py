from django import forms
from .models import User

class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already exists')
        return username

class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
