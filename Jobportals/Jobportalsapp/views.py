from django.contrib.auth import authenticate, login , logout
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages

from .models import Admin, JobSeeker , Employer , JobList, Contact, JobApplication, Category
# from .forms import JobseekerForm , LoginForm
from .forms import ContactForm,UserRegistrationForm, JobSeekerProfileForm  , EmployerProfileForm , JobForm, JobApplicationForm, CategoryForm
from django.contrib.auth.models import User

from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

from django.db.models import Count


def index(request):
    return render(request,'home.html')

def about(request):
	return render(request,'about.html')

def job_list(request):
    job_list =JobList.objects.all()
    return render(request,'job-list.html',{'job_lists':job_list})

def job_detail(request):
	return render(request,'job-detail.html')

def job_category(request):
	return render(request,'category.html')

def testimonial(request):
	return render(request,'testimonial.html')

def four(request):
	return render(request,'404.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactForm()  # Reset the form by creating a new instance
            messages.success(request, "Your message has been sent and saved successfully!")
            # Other code for handling form submission, email, etc.
    else:
        form = ContactForm()
        
    return render(request, 'contact.html', {'form': form})
        
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         # Extract form data
    #         name = form.cleaned_data['name']
    #         email = form.cleaned_data['email']
    #         subject = form.cleaned_data['subject']
    #         message = form.cleaned_data['message']

    #         # Save the form data to the Contact model (Database)
    #         Contact.objects.create( # type: ignore
    #             name=name,
    #             email=email,
    #             subject=subject,
    #             message=message
    #         )

    #         # Format the message to send via email
    #         full_message = f"Message from {name} ({email}):\n\n{message}"

    #         try:
    #             # Send the email using send_mail() function
    #             send_mail(
    #                 subject,                  # Subject of the email
    #                 full_message,             # Message content
    #                 email,                    # From email
    #                 [settings.EMAIL_HOST_USER],  # To email (the admin or the recipient)
    #                 fail_silently=False,       # If False, errors are raised
    #             )

    #             # Success message to user
    #             messages.success(request, "Your message has been sent and saved successfully!")
    #             return redirect('contact')

    #         except Exception as e:
    #             # Catch any exceptions, such as SMTPAuthenticationError
    #             messages.error(request, f"An error occurred: {e}")

    # else:
    #     form = ContactForm()

    # return render(request, 'contact.html', {'form': form})

def post_job(request):
	return render(request,'post_job.html')


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
            return redirect('index')  # Redirect after registration
        else:
            messages.error(request, "Please correct the errors in the form.")
    else:
        user_form = UserRegistrationForm()
        profile_form = JobSeekerProfileForm()

    return render(request, 'admin/jobseeker_dashboard.html', {
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

    return render(request, 'admin/login.html')  # Single login page for both user types

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout


def jobseekerDashboard(request):
    user = request.user  # This will return the currently logged-in user
    return render(request, 'index.html', {'user': user})

# List JobSeekers
def jobseeker_list(request):
    jobseekers = JobSeeker.objects.all()
    return render(request, 'admin/jobseeker_list.html', {'jobseekers': jobseekers})

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
            return redirect('index')  # Redirect after registration
        else:
            # Print detailed errors to the console for debugging
            print("User form errors:", user_form.errors)
            print("Profile form errors:", profile_form.errors)
            messages.error(request, "Please correct the errors in the form.")
    else:
        user_form = UserRegistrationForm()
        profile_form = EmployerProfileForm()

    return render(request, 'admin/employer_dashboard.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })



def employerDashboard(request):
    user = request.user  # This will return the currently logged-in user
    return render(request, 'index.html', {'user': user})

def employer_list(request):
    employer = Employer.objects.all()
    return render(request, 'admin/employer_list.html', {'employers': employer})


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
    return render(request, 'admin/admin_login.html')

def admin_logout_view(request):
    logout(request)
    messages.success(request, 'Logout successful.')
    return redirect('admin_login')

# @login_required(login_url='admin_login') # type: ignore

def admin_dashboard(request):
    if not request.user.is_superuser:
        messages.error(request,'Access restricted. Only administrator')
        return redirect('admin_dashboard')
    return render(request, 'admin/admin_dashboard.html')


def admin_job_add(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job added successfully.')
            return redirect('admin_job_list')  # Replace with your success URL
    else:
        form = JobForm()
    
    return render(request, 'admin/job_add.html', {'form': form})


def admin_success(request):
	return HttpResponse('Successfully Added')

def admin_job_list(request):    
	job_list =JobList.objects.all()

	return render(request,'admin/job_list.html',{'job_lists':job_list})

def job_edit(request, id):
    job = get_object_or_404(JobList, id=id)
    
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job updated successfully.')
            return redirect('admin_job_list')  # Redirect to the job list after editing
    else:
        form = JobForm(instance=job)
    
    return render(request, 'admin/job_edit.html', {'form': form, 'job': job})

	
def admin_job_delete(request,id):
    job_list=JobList.objects.get(id=id)
    job_list.delete()
    messages.success(request, 'Job deleted successfully.')
    return redirect("admin_job_list")


def apply_for_job_view(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save()  # Save the job application instance
            applicant_email = application.applicant_email  # Get the applicant's email
            return redirect(f'/application/success/?email={applicant_email}')  # Pass email in URL
    else:
        form = JobApplicationForm()

    return render(request, 'admin/apply_for_job.html', {'form': form})


def application_success_view(request):
    applicant_email = request.GET.get('email')  # Or from the session if necessary
    return render(request, 'admin/application_success.html', {'applicant_email': applicant_email})

    
def job_application_history_view(request):
    applicant_email = request.GET.get('email')  # Get email from query parameter

    if applicant_email:
        # Group job applications by job and count how many times each job has been applied to
        job_applications = (
            JobApplication.objects
            .filter(applicant_email=applicant_email)
            .values('job__title')  # Reference the title of the JobList model
            .annotate(application_count=Count('job'))  # Count applications per job
            .order_by('-application_count')  # Optional: order by most applied jobs
        )

        # Count total unique jobs applied to
        total_applications = len(job_applications)

        return render(request, 'admin/job_application_history.html', {
            'job_applications': job_applications,
            'total_applications': total_applications,
            'applicant_email': applicant_email
        })
    else:
        return render(request, 'admin/job_application_history.html', {'error': 'No email provided'})

def job_application_list(request):
    applications = JobApplication.objects.all()  # Retrieve all job applications
    return render(request, 'admin/job_application_list.html', {'applications': applications})


def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'admin/contact_list.html', {'contacts': contacts})


# List all categories (Read)
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'admin/category_list.html', {'categories': categories})

# Create new category
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'admin/category_form.html', {'form': form})

# Update an existing category
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'admin/category_form.html', {'form': form})

# Delete a category
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'admin/category_confirm_delete.html', {'category': category})