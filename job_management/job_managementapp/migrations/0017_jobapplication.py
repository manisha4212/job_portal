# Generated by Django 5.1 on 2024-09-26 15:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_managementapp', '0016_delete_myuser_employer_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_name', models.CharField(max_length=200)),
                ('applicant_email', models.EmailField(max_length=254)),
                ('resume', models.FileField(upload_to='resumes/')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='job_managementapp.joblist')),
            ],
        ),
    ]
