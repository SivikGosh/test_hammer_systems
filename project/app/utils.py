from random import choices
from string import ascii_letters, digits


def generate_auth_code():
    return ''.join(choices('0123456789', k=4))


def generate_invite_code():
    return ''.join(choices(ascii_letters + digits, k=6))
