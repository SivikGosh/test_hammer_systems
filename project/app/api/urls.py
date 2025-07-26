from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView

from .views import (
    InvitersAPIView,
    UserRetrieveUpdateView,
    activate_code,
    get_auth_code,
    login_by_code,
)

app_name = 'api'

urlpatterns = [
    path('auth_code/', get_auth_code, name='auth_code'),
    path('authorization/', login_by_code, name='authorization'),
    path('activate_code/', activate_code, name='activate_code'),
    path('inviters/', InvitersAPIView.as_view(), name='inviters'),
    path(
        'users/<str:phone_number>/',
        UserRetrieveUpdateView.as_view(),
        name='user'
    ),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'redoc/',
        SpectacularRedocView.as_view(url_name='api:schema'),
        name='redoc'
    ),
]
