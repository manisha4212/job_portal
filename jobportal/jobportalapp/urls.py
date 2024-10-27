from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # Job Seeker Routes
    path('jobseeker/new/', views.create_jobseeker, name='create_jobseeker'),
    path('jobseeker/list', views.jobseeker_list, name='jobseeker_list'),
    path('jobseeker/dashboard', views.jobseekerDashboard, name='jobseeker_dashboard'),
    
    #Employers Routes
    path('employeer/new/', views.create_employer, name='create_employer'),
    path('employeer/list', views.employer_list, name='employer_list'),
    path('employeer/dashboard', views.employerDashboard, name='employer_dashboard'),
    # path('index/', views.index, name='index'),
    
    #Admin Routes
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin_login/', views.admin_login_view, name='admin_login'),  # Admin login URL
    path('admin_logout/', views.admin_logout_view, name='admin_logout'),  # Admin logout URL
]
