from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Report,Message


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
          
        ]
class PoliceStaff(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
          
        ]        
        
        
class ReportForm(forms.ModelForm):
    class Meta:
        model=Report
        fields=[
            "Crime",
            "Suspect",
            "County",
            "Statement",
        ]
class MessageForm(forms.ModelForm):
    class Meta:
        model=Message
        fields=[
            "name",
            "email",
            "subject",
            "message",
        ]