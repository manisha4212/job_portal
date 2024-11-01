# Generated by Django 5.0.7 on 2024-08-07 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_managementapp', '0004_alter_customuser_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companylogo', models.ImageField(upload_to='logos/')),
                ('jname', models.CharField(max_length=50)),
                ('jcity', models.CharField(max_length=50)),
                ('jcountry', models.CharField(max_length=50)),
                ('jtime', models.TimeField()),
                ('salary_min', models.DecimalField(decimal_places=2, max_digits=10)),
                ('salary_max', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'joblist',
            },
        ),
    ]
