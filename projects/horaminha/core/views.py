from django.shortcuts import render


def eventList(request):
    return render(request, 'horaminha.html')

