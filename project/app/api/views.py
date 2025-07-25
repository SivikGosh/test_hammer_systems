from django.contrib.auth import login
from django.core.handlers.wsgi import WSGIRequest
from django.urls import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_403_FORBIDDEN,
)

from app.models import User
from app.redis import redis
from app.utils import generate_auth_code

from .serializers import AuthCodeSerializer, PhoneNumberSerializer


@api_view(('post',))
def get_auth_code(request: WSGIRequest) -> Response:
    serializer = PhoneNumberSerializer(data=request.data)
    if serializer.is_valid():
        phone_number = serializer.data.get('phone_number')
        code = generate_auth_code()
        redis.set(phone_number, code, ex=300)
        data = {'code': code, 'ttl': 300}
        return Response(data, HTTP_200_OK)
    return Response(serializer.errors, HTTP_400_BAD_REQUEST)


@api_view(('post',))
def login_by_code(request: WSGIRequest) -> Response:
    serializer = AuthCodeSerializer(data=request.data)
    if serializer.is_valid():
        phone_number = serializer.data.get('phone_number')
        auth_code = serializer.data.get('auth_code')
        code = redis.get(phone_number).decode('utf-8')
        if code == auth_code:
            user, _ = User.objects.get_or_create(phone_number=phone_number)
            login(request, user)
            redirect_url = {'redirect_url': reverse('app:start_page')}
            return Response(redirect_url, HTTP_200_OK)
        redirect_url = {'redirect_url': reverse('app:login_page')}
        return Response(serializer.errors, HTTP_403_FORBIDDEN)
    return Response(serializer.errors, HTTP_400_BAD_REQUEST)
