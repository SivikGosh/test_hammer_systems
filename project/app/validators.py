from django.core.validators import RegexValidator

phone_validator = RegexValidator(
    regex=r'^\+?[1-9]\d{9,14}$',
    message='Введите корректный номер телефона в формате +1234567890'
)
