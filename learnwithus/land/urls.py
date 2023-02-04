
from django.urls import path
from .views import *
urlpatterns = [
    path('', page1),
    path('transfer',page2),
       path('transfer/login',page3)
]
