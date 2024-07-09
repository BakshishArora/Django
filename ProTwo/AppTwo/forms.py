from django import forms
from django.core import validators
from AppTwo.models import User_Table

class NewUserForm(forms.ModelForm):
    class Meta:
        model = User_Table
        fields = '__all__'