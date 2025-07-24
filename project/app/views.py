from django.core.handlers.wsgi import WSGIRequest
from django.http.response import HttpResponse
from django.shortcuts import render

from .models import User


def start_page(request: WSGIRequest) -> HttpResponse:
    user: User = request.user
    if not user.is_authenticated:
        return render(request, 'pages/login.html')
    context_data = {'user_phone_number': user.phone_number}
    return render(request, 'pages/profile.html', context_data)
