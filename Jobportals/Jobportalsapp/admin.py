from django.contrib import admin
from .models import JobSeeker, Employer, JobList, Contact, Category
# Register your models here.

admin.site.register(JobSeeker)
admin.site.register(Employer)
admin.site.register(JobList)
admin.site.register(Contact)
admin.site.register(Category)