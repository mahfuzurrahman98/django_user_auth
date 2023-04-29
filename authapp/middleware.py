from django.shortcuts import redirect
from django.urls import reverse


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            if request.path == reverse('login') or request.path == reverse('register'):
                return self.get_response(request)
            else:
                return redirect(reverse('login'))
        else:
            if request.path == reverse('login') or request.path == reverse('register'):
                return redirect(reverse('home'))

        response = self.get_response(request)

        return response
