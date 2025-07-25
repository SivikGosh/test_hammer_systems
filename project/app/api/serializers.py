from rest_framework.serializers import (
    CharField,
    ModelSerializer,
    Serializer,
    SerializerMethodField,
)

from app.models import User
from app.validators import phone_validator


class PhoneNumberSerializer(Serializer):
    phone_number = CharField(max_length=16, validators=[phone_validator])


class AuthCodeSerializer(Serializer):
    auth_code = CharField(max_length=4)
    phone_number = CharField(max_length=16, validators=[phone_validator])


class UserSerializer(ModelSerializer):
    invite_code = SerializerMethodField()

    class Meta:
        model = User
        fields = ('phone_number', 'first_name', 'last_name', 'invite_code')

    def get_invite_code(self, obj):
        return obj.invite_code.code
