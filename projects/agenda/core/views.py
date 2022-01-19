from django.shortcuts import render, HttpResponse
from core.models import Evento

# Create your views here.

#def index(requests):
#    return redirect('/agenda') # Necessita importar render/redirect

def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.all()
    #evento = Evento.objects.filter(usuario=usuario)
    dados = { 'eventos': evento }
    return render(request, 'agenda.html', dados)