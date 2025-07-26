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
    has_activated_code = SerializerMethodField()
    activated_code = SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'phone_number',
            'first_name',
            'last_name',
            'invite_code',
            'has_activated_code',
            'activated_code',
        )

    def get_invite_code(self, obj):
        return obj.invite_code.code

    def get_has_activated_code(self, obj):
        return obj.has_activated_code

    def get_activated_code(self, obj):
        if hasattr(obj, 'activated_code') and obj.activated_code:
            return obj.activated_code.code
        return None


class ActivateCodeSerializer(Serializer):
    activate_code = CharField(max_length=6)
