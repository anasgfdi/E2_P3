from django.contrib import admin
from django.urls import path
from . import views
from .views import predict


urlpatterns = [
    path('index/', predict, name='index'),
    path('predict', views.predict, name='predict'),
]
