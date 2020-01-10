from random import randint

from .models import User

def gerar_lista_users():
    lista_usuarios = []
    while(len(lista_usuarios) < 5):
        nmr = randint(1,10)
        try:
            user = User.objects.get(pk=nmr)
            if user not in lista_usuarios:
                lista_usuarios.append(user)
        except:
            continue
    return lista_usuarios