from typing import Dict

from core.settings import site_url
from django.core.handlers.wsgi import WSGIRequest


def get_site_url(request: WSGIRequest) -> Dict[str, str]:
    return {'site_url': site_url}
