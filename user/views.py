from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework import permissions, viewsets
from django.contrib.auth.models import User
from notes.models import Notes
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]


class LoginView(TokenObtainPairView):
    def post(self, request, format=None):
        response = super().post(request, format)
        if response.status_code == 200:
            user = authenticate(username=request.data['username'], password=request.data['password'])
            response.data['user'] = UserSerializer(user, context={'request': request}).data
        return response
