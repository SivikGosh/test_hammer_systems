from django.urls import path

from .views import UserRetrieveUpdateView, get_auth_code, login_by_code

app_name = 'api'

urlpatterns = [
    path('auth_code/', get_auth_code, name='auth_code'),
    path('authorization/', login_by_code, name='authorization'),
    path(
        'users/<str:phone_number>/',
        UserRetrieveUpdateView.as_view(),
        name='user'
    ),
]
