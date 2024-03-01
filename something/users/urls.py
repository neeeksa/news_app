from django.urls import path
from . import views
from .views import login, registration

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
]
