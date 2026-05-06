from django.shortcuts import render
from django import http
from .forms import UserForm

def create_user(request):
    if (request.method == 'POST'):
        # create a form instance
        form = UserForm(request.POST)

        # check if form is valid
        if form.is_valid():
            return http.JsonResponse({'message': 'User created successfully!'}, status=201)