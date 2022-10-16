from django.urls import path
from hello import views
from .views import *

urlpatterns = [
    path('', views.hello, name='hello'),
]





