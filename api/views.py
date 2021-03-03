from rest_framework import viewsets, permissions, generics, status, exceptions
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
import requests
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from rest_framework.renderers import TemplateHTMLRenderer
import jwt, config.settings


def home(request):
    """
    Home page for instructions
    """
    return HttpResponse("<h1>Fetch external API with SimpleJWT Authentication</h1><ul><li>Go to /auth/register (Click <a href='/auth/register'>here</a>). Register a new account</li><li>Then navigate to /auth/login(Click <a href='/auth/login'>here</a>). Copy the (access and refresh) tokens</li><li>Test the API on /api/v1/foodapi/ (Click <a href='/api/v1/foodapi'>here</a>) using the access token.</li></ul>")


class foodApi(APIView):
    """
    Accept both GET & POST methods and output the results upon successful verification of access token.
    Otherwise throw error.
    """
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [AllowAny]
    http_method_names = ['get', 'post', 'head', 'options']
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'api/api_display.html'

    def post(self, request, *args, **kwargs):
        token = request.POST.get('token')
        print('payload ' + str(config.settings.SECRET_KEY))
        try:
            payload = jwt.decode(jwt=token, key=config.settings.SECRET_KEY, algorithms=['HS256'])
            print('payload 1 ' + str(payload))
            user = User.objects.get(id=payload['user_id'])
            url = "https://jsonplaceholder.typicode.com/posts"
            print(url)
            response = requests.get(url)
            data = response.json()
            print(data)
            return render(request, 'api/api_display.html', {"data":data})
            # if not user.is_active:
            #     user.is_active = True
            #     user.save()
            # return Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as e:
            return render(request, 'api/api_display.html', {'error': '0'})
        except jwt.exceptions.DecodeError as e:
            return render(request, 'api/api_display.html', {'error': '1'})

    def get(self, request, *args, **kwargs):
        return render(request, 'api/api_display.html')
