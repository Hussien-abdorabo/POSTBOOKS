from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from .models import Profile

class SignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(SignupForm, self).__init__(*args, **kwargs)
        for field in ['username','email','password1','password2']:
            self.fields[field].help_text = None    


class ProfileupdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username','email']     

    def __init__(self, *args: Any, **kwargs: Any) -> None:
            super(ProfileupdateForm, self).__init__(*args, **kwargs)
            for field in ['username','email']:
              self.fields[field].help_text = None    


class ImageupdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['image']