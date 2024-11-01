# Generated by Django 5.1 on 2024-10-05 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobportalsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companylogo', models.ImageField(upload_to='logos/')),
                ('title', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('min_salary_range', models.CharField(max_length=255)),
                ('max_salary_range', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'joblist',
            },
        ),
    ]
