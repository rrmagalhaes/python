from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

#def index(requests):
#    return redirect('/agenda') # Necessita importar render/redirect
def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario) #realiza o login
            return redirect('/')    #redirecina para página agenda
        else:
            messages.error(request, "Usuário ou senha inválido")
    return redirect('/')

@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user
    #evento = Evento.objects.all()
    evento = Evento.objects.filter(usuario=usuario)
    dados = { 'eventos': evento }
    return render(request, 'agenda.html', dados)

@login_required(login_url='/login/')
def evento(request):
    return render(request, 'evento.html')

@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        local = request.POST.get('local')
        data_evento = request.POST.get('data_evento')
        usuario = request.user
        Evento.objects.create(titulo=titulo,
                              descricao=descricao,
                              data_evento=data_evento,
                              usuario=usuario,
                              local=local)
    return redirect("/")

