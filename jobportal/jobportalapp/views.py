from django.contrib.auth import authenticate, login , logout
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Admin, JobSeeker , Employer 
# from .forms import JobseekerForm , LoginForm
from .forms import UserRegistrationForm, JobSeekerProfileForm  , EmployerProfileForm
from django.contrib.auth.models import User



def create_jobseeker(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)  # Ensure this form uses the custom user model
        profile_form = JobSeekerProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)  # Save the user instance without committing
            user.user_type = 'jobseeker'  # Set user type
            user.save()  # Save the user to the database

            jobseeker_profile = profile_form.save(commit=False)
            jobseeker_profile.user = user  # Link JobSeeker profile to the user
            jobseeker_profile.save()  # Save the JobSeeker profile

            login(request, user)  # Log in the user
            messages.success(request, "Job seeker registered successfully.")
            return redirect('login')  # Redirect after registration
        else:
            messages.error(request, "Please correct the errors in the form.")
    else:
        user_form = UserRegistrationForm()
        profile_form = JobSeekerProfileForm()

    return render(request, 'jobseeker_dashboard.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def login_view(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_type = request.POST.get('user_type')  # Either 'jobseeker' or 'employer'
      
        # Authenticate jobseeker
        if user_type == 'jobseeker':
            
            try:
                jobseeker = JobSeeker.objects.get(username=username)
                user = authenticate(request, username=jobseeker.username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('jobseeker_dashboard')  # Jobseeker dashboard URL
                else:
                    messages.error(request, 'Invalid jobseeker credentials')
            except JobSeeker.DoesNotExist:
                messages.error(request, 'Jobseeker not found')

        # Authenticate employer
        elif user_type == 'employer':
            try:
                employer = Employer.objects.get(username=username)
                user = authenticate(request, username=employer.username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('employer_dashboard')  # Employer dashboard URL
                else:
                    messages.error(request, 'Invalid employer credentials')
            except Employer.DoesNotExist:
                messages.error(request, 'Employer not found')
                
        elif user_type == 'admin':
            messages.error(request, 'first')
            try:
                messages.error(request, 'second')
                admin_user = Admin.objects.get(user__username=username)  # Get admin via related User model
                user = authenticate(request, username=admin_user.user.username, password=password)
                messages.error(request, 'third')
                
                
                if user is not None:
                    login(request, user)
                    return redirect('admin_dashboard')  # Redirect to admin dashboard
                else:
                    messages.error(request, 'Invalid admin credentials')
            except Admin.DoesNotExist:
                    messages.error(request, 'Admin not found')

    return render(request, 'login.html')  # Single login page for both user types

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout


def jobseekerDashboard(request):
    user = request.user  # This will return the currently logged-in user
    return render(request, 'index.html', {'user': user})

# List JobSeekers
def jobseeker_list(request):
    jobseekers = JobSeeker.objects.all()
    return render(request, 'jobseeker_list.html', {'jobseekers': jobseekers})

# Employer

def create_employer(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = EmployerProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.user_type = 'employer'  # Set user type
            user.save()  # Save the user to the database

            employer_profile = profile_form.save(commit=False)  # Correct the variable name here
            employer_profile.user = user  # Link Employer profile to the user
            employer_profile.save()  # Save the Employer profile

            login(request, user)  # Log in the user
            messages.success(request, "Employer registered successfully.")
            return redirect('login')  # Redirect after registration
        else:
            # Print detailed errors to the console for debugging
            print("User form errors:", user_form.errors)
            print("Profile form errors:", profile_form.errors)
            messages.error(request, "Please correct the errors in the form.")
    else:
        user_form = UserRegistrationForm()
        profile_form = EmployerProfileForm()

    return render(request, 'employer_dashboard.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })



def employerDashboard(request):
    user = request.user  # This will return the currently logged-in user
    return render(request, 'index.html', {'user': user})

def employer_list(request):
    employer = Employer.objects.all()
    return render(request, 'employer_list.html', {'employer': employer})

def admin_dashboard(request):
    # Ensure only admins can access
    if hasattr(request.user, 'admin'):
        return render(request, 'admin_dashboard.html')
    else:
        return redirect('admin_login')

def index(request):
    return render(request,'index.html')


def admin_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_superuser:
                login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('admin_dashboard')  # Redirect to a view name 'dashbord'
            else:
                messages.error(request, 'This page is only accessible by admin.')
                return redirect('/admin/login/')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('admin_login')
    # Render the login template
    return render(request, 'admin_login.html')

def admin_logout_view(request):
    logout(request)
    messages.success(request, 'Logout successful.')
    return redirect('admin_login')

# @login_required(login_url='admin_login') # type: ignore

def admin_dashboard(request):
    if not request.user.is_superuser:
        messages.error(request,'Access restricted. Only administrator')
        return redirect('dashbord')
    return render(request, 'admin_dashboard.html')