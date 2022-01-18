from django.shortcuts import render, HttpResponse
from core.models import Evento

# Create your views here.

def events(request, titulo_evento):
    titulo = Evento.objects.get(titulo=titulo_evento)
    return HttpResponse(f'<h1>{titulo}</h1>')