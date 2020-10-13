from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def consulta_evento(request, nome_evento):
    nome_evento = Evento.objects.get(titulo=nome_evento)
    return HttpResponse(f'<h1>Evento Agendado: {nome_evento}<h1>')

def login_user(request):
    return render(request, 'login.html')    # return httpresponse object

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "usuario ou senha invalida")
    return redirect('/')

@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user

    # usuario = request.user
    # evento = Evento.objects.filter(usuario=usuario)
    # evento = Evento.objects.all()  # primeiro
    evento = Evento.objects.filter(usuario=usuario)
    response = {'eventos': evento}
    return render(request, 'agenda.html', response)

# def index(request):
#     return redirect('/agenda/')