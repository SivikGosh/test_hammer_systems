from django.core.handlers.wsgi import WSGIRequest
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from .models import User


def start_page(request: WSGIRequest) -> HttpResponseRedirect | HttpResponse:
    user: User = request.user
    if not user.is_authenticated:
        return redirect(reverse('app:login_page'))
    context_data = {'user_phone_number': user.phone_number}
    return render(request, 'pages/profile.html', context_data)


def login_page(request: WSGIRequest) -> HttpResponse:
    return render(request, 'pages/login.html')
