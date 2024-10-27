from django import forms
from .models import JobSeeker , Employer , JobList, JobApplication, Category,Contact
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
  
class JobForm(forms.ModelForm):
    class Meta:
        model = JobList
        fields = ['companylogo', 'title', 'city', 'country', 'type', 'min_salary_range','max_salary_range']  # Include all fields you need


class JobApplicationForm(forms.ModelForm):
    job = forms.ModelChoiceField(queryset=JobList.objects.all(), required=True)

    class Meta:
        model = JobApplication
        fields = ['job', 'applicant_name', 'applicant_email', 'resume']
        
        
# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Your Name'}))
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your Email'}))
#     subject = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
#     message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your Message'}))

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }

    
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'icon_class', 'vacancy_count']
