from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from core.models import Evento

def consulta_evento(request, nome_evento):
    nome_evento = Evento.objects.get(titulo=nome_evento)
    return HttpResponse(f'<h1>Evento Agendado: {nome_evento}<h1>')

def lista_eventos(request):
    # usuario = request.user
    # evento = Evento.objects.filter(usuario=usuario)
    evento = Evento.objects.all()  # primeiro
    response = {'eventos': evento}
    return render(request, 'agenda.html', response)

# def index(request):
#     return redirect('/agenda/')