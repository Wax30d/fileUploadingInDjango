from django import forms
from .models import User_Profile


class Profile_Form(forms.ModelForm):
    class Meta:
        model = User_Profile
        fields = [
            'fname',
            'lname',
            'technologies',
            'email',
            'display_picture'
        ]
