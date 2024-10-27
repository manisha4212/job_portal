from django.contrib import admin
from .models import JobList ,CustomUser  ,JobApplication

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(JobList)
# admin.site.register(Jobseeker)
# admin.site.register(Employer)
admin.site.register(JobApplication)