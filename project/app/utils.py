from random import choices


def generate_auth_code():
    return ''.join(choices('0123456789', k=4))
