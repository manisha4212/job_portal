# Generated by Django 5.1 on 2024-10-04 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_managementapp', '0020_alter_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('jobseeker', 'Job Seeker'), ('employer', 'Employer'), ('admin', 'Admin')], max_length=10),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(default='default_username', max_length=150, unique=True),
        ),
    ]
