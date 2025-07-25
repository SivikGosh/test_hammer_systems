from rest_framework.serializers import CharField, ModelSerializer, Serializer

from app.models import User
from app.validators import phone_validator


class PhoneNumberSerializer(Serializer):
    phone_number = CharField(max_length=16, validators=[phone_validator])


class AuthCodeSerializer(Serializer):
    auth_code = CharField(max_length=4)
    phone_number = CharField(max_length=16, validators=[phone_validator])


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('phone_number', 'first_name', 'last_name')
