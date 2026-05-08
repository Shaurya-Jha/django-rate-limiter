import json
from django import http
from django.utils import timezone
from .forms import UserForm
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        try:
            # Parse the JSON body
            data = json.loads(request.body)
            # Pass the dictionary to the form
            form = UserForm(data) 
        except json.JSONDecodeError:
            return http.JsonResponse({'error': 'Invalid JSON'}, status=400)

        if form.is_valid():
            user = form.save(commit=False)
            user.date_joined = timezone.now()
            user.save()
            return http.JsonResponse({'message': 'User created successfully!'}, status=201)
        
        return http.JsonResponse({'errors': form.errors}, status=400)

    return http.JsonResponse({'error': 'Method not allowed'}, status=405)
