# from django.contrib.auth.models import BaseUserManager

# class UserManager(BaseUserManager):
#     def create_user(self,user_name, email, password=None, **extra_fields):
#         if not user_name:
#             raise ValueError('The PhoneNumber Field must be set')
#         email = self.normalize_email(email)
#         user = self.model(user_name=user_name, email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self.db)
#         return user
    
#     def create_superuser(self, user_name, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff',True)
#         extra_fields.setdefault('is_superuser',True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
        
#         return self.create_user(user_name, email, password, **extra_fields)