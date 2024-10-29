
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        

        # Basic validations
        if not all([name, email, password, confirm_password]):
            messages.error(request, "Please fill all fields")
            return redirect('register')
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')
        if User.objects.filter(username=email).exists():
            messages.error(request, "Email is already registered.")
            return redirect('register')

        # Create user
        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = name  # Saving user's name in first_name field
        user.save()

        # Log the user in and redirect
        login(request, user)
        return redirect('index')  # Redirect to home page or another page

    return render(request, 'register.html')
def Log_in(request):
    if request.POST:
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
    return render(request,'login.html')

def log_out(request):
    logout(request)
    return redirect('index')
