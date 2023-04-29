from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

# Create your views here.


def login(request):
    return render(request, 'authapp/login.html')


def register(request):

    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # print(first_name, last_name, username, email, password, confirm_password)
        # return

        # Check if passwords match
        if password == confirm_password:
            # Check if username exists
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'That email is being used')
                return redirect('/authapp/register')
            else:
                # Looks good
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                # Login after register
                # auth.login(request, user)
                # messages.success(request, 'You are now logged in')
                # return redirect('index')
                user.save()
                messages.success(request, 'You are now registered and can log in')
                return redirect('/authapp/login')

        else:
            messages.error(request, 'Passwords do not match')
            return redirect('/authapp/register')
        
    elif request.method == 'GET':
      return render(request, 'authapp/register.html')
  
    else:
      messages.error(request, 'Invalid request')


def home(request):
    return render(request, 'authapp/home.html')
    