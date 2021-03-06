from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics, validators, status
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth.models import User
from .serializers import RegisterSerializer

import random

class RegisterView(generics.CreateAPIView):
    """
    Register serializer
    """
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
