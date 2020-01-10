from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'user_unlogged/index.html')

def criar_conta(request):
    return render(request,'user_unlogged/criar_conta.html')

def logar(request):
    return render(request,'user_unlogged/login.html')

