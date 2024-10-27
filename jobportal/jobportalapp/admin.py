from django.contrib import admin

# Register your models here.

from .models import JobSeeker , CustomUser , Employer

admin.site.register(JobSeeker)
admin.site.register(Employer)
admin.site.register(CustomUser)