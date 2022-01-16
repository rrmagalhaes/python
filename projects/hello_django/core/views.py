from django.shortcuts import render, HttpResponse


# Create your views here.

def hello(request, nome):
    return HttpResponse(f'<h1>Hello {nome}</h1>')


def soma(request, n1, n2):
    somaN = n1 + n2
    return HttpResponse(f'<h1>A soma de {n1} + {n2} = {somaN}</h1>')


def subtracao(request, n1, n2):
    subtracaoN = int(n1) - int(n2)
    return HttpResponse(f'<h1>A subtração de {n1} - {n2} = {subtracaoN}</h1>')


def multiplicacao(request, n1, n2):
    multiplicacaoN = int(n1) * int(n2)
    return HttpResponse(f'<h1>A multiplicação de {n1} por {n2} = {multiplicacaoN}</h1>')


def divisao(request, n1, n2):
    if int(n2) > 0:
        divisaoN = int(n1) / int(n2)
        return HttpResponse(f'<h1>A divisão de {n1} por {n2} = {divisaoN}</h1>')
    else:
        return HttpResponse(f'<h1>Só é possível a divisão por números acima de 0!</h1>')
