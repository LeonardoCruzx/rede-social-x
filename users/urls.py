from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('pagina-inicial',pagina_inicial_usuario,name='pagina-inicial-usuario')
]