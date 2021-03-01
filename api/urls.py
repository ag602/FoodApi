from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from . import views

router = routers.DefaultRouter()


urlpatterns = [

    path('v1/', include(router.urls)),
    path('v1/foodapi/', views.foodApi.as_view()),

]

