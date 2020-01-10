from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('',index,name='index'),
    path('criar-conta',criar_conta,name='criar-conta'),
    path('login',logar,name='login'),
]
