from django import forms
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm, UserChangeForm as BaseUserChangeForm
from cleanscreenapi.models import User

class UserCreationForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add password fields
        self.fields['password1'].widget = forms.PasswordInput()
        self.fields['password2'].widget = forms.PasswordInput()

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already exists')
        return username

    def save(self, commit=True):
        user = super().save(commit=False)
        # Set the password correctly
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class UserChangeForm(BaseUserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')