from django.urls import path
from .views import create_user

urlpatterns = [
    path('/create', create_user, name='create_new_user')
]