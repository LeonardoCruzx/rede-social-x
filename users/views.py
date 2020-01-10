from django.shortcuts import render

from posts.models import Post

from .script1 import gerar_lista_users

# Create your views here.
def pagina_inicial_usuario(request):
    context = {}
    context["posts"] = Post.objects.all()
    context["possiveis_contatos"] = gerar_lista_users()
    return render(request,'user_logged/pagina_inicial.html',context)