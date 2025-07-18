from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

def animal_view(request):
    user = User.objects.first()
    refresh = RefreshToken.for_user(user)
    context = {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    return render(request, 'animal-list.html',context)