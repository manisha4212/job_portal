# from django.shortcuts import render

# # Create your views here.

# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages

# def admin_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             if user.is_superuser:
#                 login(request, user)
#                 #messages.success(request, 'Login successful.')
#                 return redirect('admin_dashboard')  # Redirect to a view name 'dashboard'
#             else:
#                 messages.error(request, 'This page is only accessible by admin.')
#                 return redirect('/admin/login/')
#         else:
#             messages.error(request, 'Invalid username or password.')
#             return redirect('admin_login')
#     # Render the login template
#     return render(request, 'admin/login.html')

# def admin_logout(request):
#     logout(request)
#     #messages.success(request, 'Logout successful.')
#     return redirect('admin_login')
