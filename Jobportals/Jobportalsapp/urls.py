from django.urls import path
from . import views

urlpatterns = [
    
    path('index/',views.index, name='index'),
	path('about/',views.about, name='about'),
	path('job_list/',views.job_list, name='job_list'),
	path('job_detail/',views.job_detail, name='job_detail'),
	path('job_category/',views.job_category, name='job_category'),
    path('testimonial/',views.testimonial, name='testimonial'),
    path('four/',views.four, name='four'),
	path('contact/',views.contact, name='contact'),
    path('post_job/',views.post_job, name='post_job'),
    
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Job Seeker Routes
    path('jobseeker/new/', views.create_jobseeker, name='create_jobseeker'),
    path('jobseeker_list', views.jobseeker_list, name='jobseeker_list'),
    path('jobseeker/dashboard', views.jobseekerDashboard, name='jobseeker_dashboard'),
    
    #Employers Routes
    path('employeer/new/', views.create_employer, name='create_employer'),
    path('employeer_list', views.employer_list, name='employer_list'),
    path('employeer/dashboard', views.employerDashboard, name='employer_dashboard'),
    
    
    #Admin Routes
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin_login/', views.admin_login_view, name='admin_login'),  # Admin login URL
    path('admin_logout/', views.admin_logout_view, name='admin_logout'),  # Admin logout URL
    

	path('admin_job_add/', views.admin_job_add, name='admin_job_add'),
    path('admin_jobs_list', views.admin_job_list, name='admin_job_list'),
    path('admin/success/',views.admin_success, name='admin_success'),
    path('admin_job_edit/<int:id>/', views.job_edit, name='admin_job_edit'),
	path('admin_job_delete/<str:id>',views.admin_job_delete,name='admin_job_delete'),
 
    path('jobs/apply/', views.apply_for_job_view, name='apply_for_job'),
    path('application/success/', views.application_success_view, name='application_success'),
    path('application/history/', views.job_application_history_view, name='job_application_history'),
    path('applications/', views.job_application_list, name='job_application_list'),
 
    # path('contact_admin/', views.contact_admin, name='contact_admin'),
    path('contact_list/', views.contact_list, name='contact_list'),
    
    path('categories/', views.category_list, name='category_list'),
    path('categories/new/', views.category_create, name='category_create'),
    path('categories/<int:pk>/edit/', views.category_update, name='category_update'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),
]
