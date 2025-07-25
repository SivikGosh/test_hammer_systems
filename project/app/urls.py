from django.urls import path

from .views import login_page, start_page

app_name = 'app'

urlpatterns = [
    path('', start_page, name='start_page'),
    path('login/', login_page, name='login_page'),
]
