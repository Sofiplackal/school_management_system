from django import forms
from django.contrib.auth.models import User
from . import models

# For admin signup
class AdminSigupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)  # Use PasswordInput widget for passwords
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']


# For student related form
class StudentUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)  # Use PasswordInput widget for passwords
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']


class StudentExtraForm(forms.ModelForm):
    class Meta:
        model = models.StudentExtra
        fields = ['roll', 'cl', 'mobile', 'fee', 'status']


# For teacher related form
class TeacherUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)  # Use PasswordInput widget for passwords
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']


class TeacherExtraForm(forms.ModelForm):
    class Meta:
        model = models.TeacherExtra
        fields = ['salary', 'mobile', 'status']


# For Attendance related form
presence_choices = [('Present', 'Present'), ('Absent', 'Absent')]

class AttendanceForm(forms.Form):
    present_status = forms.ChoiceField(choices=presence_choices)
    date = forms.DateField()


class AskDateForm(forms.Form):
    date = forms.DateField()


# For notice related form
class NoticeForm(forms.ModelForm):
    class Meta:
        model = models.Notice
        fields = '__all__'


# For Contact Us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))
