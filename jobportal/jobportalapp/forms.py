from django import forms
from .models import JobSeeker , Employer
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model



class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()  # This will reference your custom user model
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])  # Hash the password
        if commit:
            user.save()
        return user


class JobSeekerProfileForm(forms.ModelForm):
    class Meta:
        model = JobSeeker
        fields = ['fname', 'lname', 'gender', 'dob', 'city', 'country', 'username', 'resume', 'address', 'skills']


class EmployerProfileForm(forms.ModelForm):
	class Meta:
		model = Employer
		fields = ['company_name', 'employer_name', 'employer_phone', 'employer_email', 'username']
  
