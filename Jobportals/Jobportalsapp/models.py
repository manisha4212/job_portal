from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.models import User
from django.conf import settings 
from django.contrib.auth import get_user_model

# from .manager import UserManager



# Extend the default Django User model
class CustomUser(AbstractUser):
    user_type = models.CharField(max_length=10, choices=[('jobseeker', 'Job Seeker'), ('employer', 'Employer'),  ('admin', 'Admin'),])
    # username = models.CharField(unique=True, max_length=25)
    # email = models.EmailField(unique=True)

    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['email']

    # objects = UserManager()

class JobSeeker(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Add other job seeker fields here
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    dob = models.DateField()
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    resume = models.FileField(upload_to='resumes/')
    address = models.CharField(max_length=100)
    skills = models.CharField(max_length=255)  # Added max_length

    class Meta:
        db_table = "jobseeker"

    def __str__(self):
        return self.user.username



class Employer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Add other employer fields here
    username = models.CharField(max_length=50)
    company_name = models.CharField(max_length=20)
    employer_name = models.CharField(max_length=50)
    employer_phone = models.CharField(max_length=50)
    employer_email = models.EmailField(max_length=50)
    class Meta:
        db_table = "employer" 
         
    def __str__(self):
        return self.user.username

class Admin(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)

    # Add other admin fields here
    class Meta:
        db_table = "admin" 
         
    def __str__(self):
        return self.user.username
    
class JobList(models.Model):
    companylogo = models.ImageField(upload_to='logos/')
    title = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    min_salary_range = models.CharField(max_length=255) # Minimum salary
    max_salary_range = models.CharField(max_length=255)

    class Meta:
        db_table = 'joblist'

    def __str__(self):
        return self.title
    
    
class JobApplication(models.Model):
    job = models.ForeignKey(JobList, on_delete=models.CASCADE, related_name='applications')
    applicant_name = models.CharField(max_length=200)
    applicant_email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')  # Assumes you have media settings configured

    def __str__(self):
        return f"{self.applicant_name} applied for {self.job.title}"
    
    
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
    
    class Meta:
        db_table = "contact"
        
        
class Category(models.Model):
    name = models.CharField(max_length=255)
    icon_class = models.CharField(max_length=255)  # For storing the icon class, e.g., 'fa-mail-bulk'
    vacancy_count = models.IntegerField()

    def __str__(self):
        return self.name