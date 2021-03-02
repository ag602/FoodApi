from rest_framework import viewsets, permissions, generics, status, exceptions
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
import requests
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework.permissions import IsAuthenticated


class foodApi(APIView):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'head', 'options']

    def get(self, request, *args, **kwargs):
        url = "https://jsonplaceholder.typicode.com/posts"
        response = requests.get(url)
        data = response.json()
        new_dict = {}
        for i, j in enumerate(data):
            new_dict[i] = j
        print(new_dict)
        return Response(new_dict, status=200)

