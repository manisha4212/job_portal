from django.urls import path
from .import views

from django.contrib.auth.views import LogoutView


urlpatterns=[
	path('index/',views.index, name='index'),
	path('about/',views.about, name='about'),
	path('job_list/',views.job_list, name='job_list'),
	path('job_detail/',views.job_detail, name='job_detail'),
	path('job_category/',views.job_category, name='job_category'),
    path('testimonial/',views.testimonial, name='testimonial'),
    path('four/',views.four, name='four'),
	path('contact/',views.contact, name='contact'),
    path('post_job/',views.post_job, name='post_job'),
    
    # path('register/',views.register,name='register'),
	# path('home',views.home, name='home'),
	# path('logout/',views.logout_view, name='logout'),
    # Admin routes
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
	path('admin/users/', views.admin_users, name='admin_users'),
	path('admin/job_add/', views.admin_job_add, name='admin_job_add'),
    path('admin/jobs/', views.admin_job_list, name='admin_job_list'),
    path('admin/success/',views.admin_success, name='admin_success'),

    path('admin/job/edit/<int:id>/', views.job_edit, name='admin_job_edit'),
	path('admin/job/delete/<str:id>',views.admin_job_delete),
    
	# path('jobseeker_register/',views.jobseeker_register, name='jobseeker_register'), 
    # path('jobseeker_login/',views.jobseeker_login, name='jobseeker_login'), 
    # path('jobseeker_list/',views.jobseeker_list, name='jobseeker_list'), 
    # path('jobseeker_logout/', LogoutView.as_view(), name='jobseeker_logout'),
 
    # path('employer_register/',views.employer_register, name='employer_register'),
    # path('employer_login/',views.employer_login, name='employer_login'),  # Login URL
    # path('employer_logout/',views.employer_logout, name='employer_logout'),
	# path('employer_list/',views.employer_list , name='employer_list'),
	 

    path('jobs/apply/', views.apply_for_job_view, name='apply_for_job'),
    path('application/success/', views.application_success_view, name='application_success'),
	path('my-applications/', views.my_job_applications_view, name='my_job_applications'),
 
 
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

    