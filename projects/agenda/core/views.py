from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http.response import Http404, JsonResponse


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
    data_atual = datetime.now() - timedelta(hours=3)
    try:
        evento = Evento.objects.filter(usuario=usuario,
                                   data_evento__gt=data_atual)
    except Exception:
        raise Http404
    dados = { 'eventos': evento }
    return render(request, 'agenda.html', dados)

@login_required(login_url='/login/')
def evento(request):
    try:
        id_evento = request.GET.get('id')
    except Exception:
        raise Http404
    dados = {}
    if id_evento:
        dados['evento'] = Evento.objects.get(id=id_evento)
    return render(request, 'evento.html', dados)

@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        local = request.POST.get('local')
        data_evento = request.POST.get('data_evento')
        usuario = request.user
        id_evento = request.POST.get('id_evento')
        if id_evento:
            try:
                evento = Evento.objects.get(id=id_evento)
            except Exception:
                raise Http404
            if evento.usuario == usuario:
                evento.titulo = titulo
                evento.descricao = descricao
                evento.data_evento = data_evento
                evento.local = local
                evento.save()
            #Evento.objects.filter(id=id_evento).update(titulo=titulo,
            #                                           data_evento=data_evento,
            #                                           descricao=descricao,
            #                                           local=local)
        else:
            Evento.objects.create(titulo=titulo,
                                  descricao=descricao,
                                  data_evento=data_evento,
                                  usuario=usuario,
                                  local=local)
    return redirect("/")

@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    try:
        evento = Evento.objects.get(id=id_evento)
    except Exception:
        raise Http404
    if usuario == evento.usuario:
        evento.delete()
    else:
        raise Http404()
    return redirect('/')

#@login_required(login_url='/login/')
def json_lista_eventos(request, id_usuario):
    usuario = User.objects.get(id=id_usuario)
    #evento = Evento.objects.all()
    try:
        evento = Evento.objects.filter(usuario=usuario).values('id', 'titulo')
    except Exception:
        raise Http404
    return JsonResponse(list(evento), safe=False)

@login_required(login_url='/login/')
def lista_eventos_historico(request):
    usuario = request.user

    #evento = Evento.objects.all()
    data_atual = datetime.now()
    try:
        evento = Evento.objects.filter(usuario=usuario,
                                   data_evento__lt=data_atual)
    except Exception:
        raise Http404
    dados = { 'eventos': evento }
    return render(request, 'historico.html', dados)