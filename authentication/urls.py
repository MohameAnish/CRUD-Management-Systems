from django.urls import path
from .views import *     

urlpatterns = [
     path('', LoginPage, name='login'),
     path('logout/', LogoutPage, name='logout')
]
