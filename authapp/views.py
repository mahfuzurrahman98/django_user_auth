from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .signupform import SignUpForm

# Create your views here.


def login(request):
    return render(request, 'authapp/login.html')


def register(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Get form values
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']

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
                    user = User.objects.create_user(
                        username=username,
                        password=password,
                        email=email, first_name=first_name,
                        last_name=last_name
                    )
                    user.save()
                    messages.success(
                        request, 'You are now registered and can log in')
                    return redirect('/authapp/login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
            return redirect('/authapp/register')

    elif request.method == 'GET':
        return render(request, 'authapp/register.html')

    else:
        messages.error(request, 'Invalid request')


def home(request):
    return render(request, 'authapp/home.html')
