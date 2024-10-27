from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import JobList , JobApplication , JobSeeker , Employer

class JobForm(forms.ModelForm):
    class Meta:
        model = JobList
        fields = ['companylogo', 'title', 'city', 'country', 'type', 'min_salary_range','max_salary_range']  # Include all fields you need

class JobApplicationForm(forms.ModelForm):
    job = forms.ModelChoiceField(queryset=JobList.objects.all(), required=True)

    class Meta:
        model = JobApplication
        fields = ['job', 'applicant_name', 'applicant_email', 'resume']
        
        
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
		fields = ['company_name', 'employer_name', 'employer_phone','experiance', 'employer_email', 'username']
  