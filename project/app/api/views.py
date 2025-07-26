from django.contrib.auth import login
from django.core.exceptions import ObjectDoesNotExist
from django.core.handlers.wsgi import WSGIRequest
from django.urls import reverse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
    HTTP_418_IM_A_TEAPOT,
)

from app.models import ActivatedCode, InviteCode, User
from app.redis import redis
from app.utils import generate_auth_code

from .serializers import (
    ActivateCodeSerializer,
    AuthCodeSerializer,
    PhoneNumberSerializer,
    UserSerializer,
)


class UserRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'phone_number'


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



@api_view(('post',))
@permission_classes((AllowAny,))
def activate_code(request: WSGIRequest) -> Response:
    serializer = ActivateCodeSerializer(data=request.data)
    if serializer.is_valid():
        code = serializer.data.get('activate_code')
        user = User.objects.get(phone_number=request.user.phone_number)
        data = {'message': None}
        if user.has_activated_code:
            data['message'] = 'Ты уже активировали код.'
            return Response(data, HTTP_418_IM_A_TEAPOT)
        try:
            invite_code = InviteCode.objects.get(code=code)
            if invite_code == user.invite_code:
                data['message'] = 'Нельзя активировать собственный код.'
                return Response(data, HTTP_403_FORBIDDEN)
        except ObjectDoesNotExist:
            data['message'] = 'Несуществующий код.'
            return Response(data, HTTP_404_NOT_FOUND)
        _, _ = ActivatedCode.objects.get_or_create(user=user, code=invite_code)
        data['message'] = 'Код активирован.'
        return Response(data, HTTP_200_OK)
    return Response(serializer.errors, HTTP_400_BAD_REQUEST)
