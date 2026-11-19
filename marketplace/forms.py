from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    # Add the role choice to the registration form
    role = forms.ChoiceField(choices=Profile.ROLE_CHOICES, required=True, label="I am a...")

    class Meta:
        model = User
        fields = ['username', 'email', 'role']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            # Update the automatically created profile with the chosen role
            user.profile.role = self.cleaned_data['role']
            user.profile.save()
        return user